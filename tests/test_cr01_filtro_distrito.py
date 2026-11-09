"""Pruebas del filtro por distrito (CR01).

PR-07 / CR01.
"""

import csv
from pathlib import Path
import pytest

from panviz.importador import importar
from panviz.validador import validar
from panviz.filtro import filtrar_por_distrito
from panviz.consolidador import consolidar
from panviz.exportador import exportar


def _cargar_oraculo_distrito(distrito: str) -> list[dict]:
    with open("datos/oraculo_consolidado.csv", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return [
            {
                "semana_iso": r["semana_iso"],
                "establecimiento": r["establecimiento"],
                "distrito": r["distrito"],
                "grupo_etario": r["grupo_etario"],
                "casos": int(r["casos"]),
            }
            for r in reader
            if r["distrito"] == distrito
        ]


def test_cr01_coincidencia_fila_por_fila_oraculo():
    """PR-07 / CR01: Consolidado filtrado coincide fila por fila con oraculo_consolidado.csv (6, 5, 4)."""
    filas = importar(Path("datos/notificaciones_iras_sinteticas.csv"))
    validas, _ = validar(filas)

    totales_esperados = {"Cercado": 6, "Cayma": 5, "Yanahuara": 4}

    for distrito, total_esp in totales_esperados.items():
        filtradas, aceptadas_dist = filtrar_por_distrito(validas, distrito)
        consol_filtrado = consolidar(filtradas)
        oraculo_dist = _cargar_oraculo_distrito(distrito)

        assert aceptadas_dist == total_esp
        assert len(consol_filtrado) == len(oraculo_dist)
        assert sum(r["casos"] for r in consol_filtrado) == total_esp

        for i, (obs, esp) in enumerate(zip(consol_filtrado, oraculo_dist)):
            assert (
                obs == esp
            ), f"Discrepancia en distrito {distrito}, fila {i}: {obs} != {esp}"


def test_cr01_suma_tres_distritos_igual_quince():
    """PR-07 / CR01: La suma de los consolidados de los 3 distritos es 15, igual a la salida sin filtro."""
    filas = importar(Path("datos/notificaciones_iras_sinteticas.csv"))
    validas, _ = validar(filas)

    total_sin_filtro = sum(r["casos"] for r in consolidar(validas))
    assert total_sin_filtro == 15

    suma_particion = 0
    for distrito in ["Cercado", "Cayma", "Yanahuara"]:
        filtradas, _ = filtrar_por_distrito(validas, distrito)
        suma_particion += sum(r["casos"] for r in consolidar(filtradas))

    assert suma_particion == 15
    assert suma_particion == total_sin_filtro


def test_cr01_normalizacion_mayusculas_y_espacios():
    """PR-07 / CR01: El filtro ignora mayúsculas/minúsculas y espacios en extremos ('cayma', ' CAYMA ')."""
    filas = importar(Path("datos/notificaciones_iras_sinteticas.csv"))
    validas, _ = validar(filas)

    variantes = ["Cayma", "cayma", " CAYMA ", "  cayma  "]
    referencia = consolidar(filtrar_por_distrito(validas, "Cayma")[0])

    for var in variantes:
        filtradas, n_aceptadas = filtrar_por_distrito(validas, var)
        consol = consolidar(filtradas)
        assert n_aceptadas == 5
        assert consol == referencia


def test_cr01_invariabilidad_de_rechazos(tmp_path: Path):
    """PR-07 / CR01: rechazos.csv es idéntico con o sin filtro (5 rechazos)."""
    filas = importar(Path("datos/notificaciones_iras_sinteticas.csv"))
    validas, rechazos = validar(filas)

    dir_sin = tmp_path / "sin_filtro"
    dir_con = tmp_path / "con_filtro"

    exportar(consolidar(validas), rechazos, dir_sin, len(filas))
    filtradas, n_dist = filtrar_por_distrito(validas, "Cercado")
    exportar(
        consolidar(filtradas),
        rechazos,
        dir_con,
        len(filas),
        distrito_filtrado="Cercado",
        aceptadas_del_distrito=n_dist,
    )

    rechazos_sin = (dir_sin / "rechazos.csv").read_bytes()
    rechazos_con = (dir_con / "rechazos.csv").read_bytes()
    assert rechazos_sin == rechazos_con
    assert len(rechazos) == 5


def test_cr01_resumen_contextual_con_filtro(tmp_path: Path):
    """PR-07 / CR01: resumen.txt con filtro contiene leidas=20, aceptadas=15, rechazadas=5, distrito_filtrado y aceptadas_del_distrito."""
    filas = importar(Path("datos/notificaciones_iras_sinteticas.csv"))
    validas, rechazos = validar(filas)

    filtradas, n_dist = filtrar_por_distrito(validas, "Yanahuara")
    codigo = exportar(
        consolidar(filtradas),
        rechazos,
        tmp_path,
        len(filas),
        distrito_filtrado="Yanahuara",
        aceptadas_del_distrito=n_dist,
    )
    assert codigo == 0

    contenido = (tmp_path / "resumen.txt").read_text(encoding="utf-8")
    lineas = dict(
        line.split(":", 1)
        for line in contenido.strip().splitlines()
        if ":" in line
    )

    assert lineas["leidas"].strip() == "20"
    assert lineas["aceptadas"].strip() == "15"
    assert lineas["rechazadas"].strip() == "5"
    assert lineas["distrito_filtrado"].strip() == "Yanahuara"
    assert lineas["aceptadas_del_distrito"].strip() == "4"
    assert lineas["suma_consolidado"].strip() == "4"
    assert lineas["diferencia_reconciliacion"].strip() == "0"


def test_cr01_distrito_sin_registros_aceptados(tmp_path: Path):
    """PR-07 / CR01: Distrito sin registros aceptados produce consolidado solo con encabezado, suma 0 y aviso."""
    filas = importar(Path("datos/notificaciones_iras_sinteticas.csv"))
    validas, rechazos = validar(filas)

    filtradas, n_dist = filtrar_por_distrito(validas, "DistritoInexistente")
    codigo = exportar(
        consolidar(filtradas),
        rechazos,
        tmp_path,
        len(filas),
        distrito_filtrado="DistritoInexistente",
        aceptadas_del_distrito=n_dist,
    )
    assert codigo == 0
    assert n_dist == 0

    # Consolidado solo encabezado
    with open(tmp_path / "consolidado.csv", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        encabezado = next(reader)
        filas_consol = list(reader)

    assert encabezado == [
        "semana_iso",
        "establecimiento",
        "distrito",
        "grupo_etario",
        "casos",
    ]
    assert len(filas_consol) == 0

    # Resumen
    texto_resumen = (tmp_path / "resumen.txt").read_text(encoding="utf-8")
    assert "distrito_filtrado: DistritoInexistente" in texto_resumen
    assert "aceptadas_del_distrito: 0" in texto_resumen
    assert "suma_consolidado: 0" in texto_resumen
    assert "diferencia_reconciliacion: 0" in texto_resumen
    assert (
        "AVISO: el distrito 'DistritoInexistente' no presenta registros aceptados."
        in texto_resumen
    )


def test_cr01_paridad_byte_a_byte_sin_filtro(tmp_path: Path):
    """PR-07 / CR01: Sin filtro, los 3 archivos de salida son idénticos byte a byte a evidencias/ejecucion_v0/."""
    filas = importar(Path("datos/notificaciones_iras_sinteticas.csv"))
    validas, rechazos = validar(filas)

    # Exportar sin filtro
    codigo = exportar(consolidar(validas), rechazos, tmp_path, len(filas))
    assert codigo == 0

    archivos = ["consolidado.csv", "rechazos.csv", "resumen.txt"]
    for arch in archivos:
        obs = (tmp_path / arch).read_bytes()
        esp = (Path("evidencias/ejecucion_v0") / arch).read_bytes()
        assert (
            obs == esp
        ), f"Diferencia byte a byte detectada en {arch} contra evidencias/ejecucion_v0/"
