"""Pruebas de exportación, formato de archivos y reconciliación.

PR-06 (R04).
"""

import csv
from pathlib import Path

from panviz.importador import importar
from panviz.validador import validar
from panviz.consolidador import consolidar
from panviz.exportador import exportar


def test_reconciliacion_y_archivos_exportados(tmp_path: Path):
    """PR-06 (R04): Reconciliación exitosa (0), encabezados y coincidencia con oráculos."""
    filas = importar(Path("datos/notificaciones_iras_sinteticas.csv"))
    validas, rechazos = validar(filas)
    consolidado = consolidar(validas)

    codigo = exportar(consolidado, rechazos, tmp_path, total_leidas=len(filas))
    assert codigo == 0

    # 1. Verificar generación y encabezados exactos
    archivo_consol = tmp_path / "consolidado.csv"
    archivo_rechaz = tmp_path / "rechazos.csv"
    archivo_resum = tmp_path / "resumen.txt"

    assert archivo_consol.exists()
    assert archivo_rechaz.exists()
    assert archivo_resum.exists()

    with open(archivo_consol, encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        encabezado_consol = next(reader)
        assert encabezado_consol == ["semana_iso", "establecimiento", "distrito", "grupo_etario", "casos"]

    with open(archivo_rechaz, encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        encabezado_rechaz = next(reader)
        assert encabezado_rechaz == ["fila_datos", "id", "motivo"]

    # 2. Verificar contenido de rechazos contra datos/oraculo_rechazos.csv
    with open(archivo_rechaz, encoding="utf-8", newline="") as f:
        reader_obs = csv.DictReader(f)
        filas_rechazos_obs = list(reader_obs)

    with open("datos/oraculo_rechazos.csv", encoding="utf-8", newline="") as f:
        reader_esp = csv.DictReader(f)
        filas_rechazos_esp = list(reader_esp)

    assert len(filas_rechazos_obs) == len(filas_rechazos_esp)
    for obs, esp in zip(filas_rechazos_obs, filas_rechazos_esp):
        assert obs["fila_datos"] == esp["fila_datos"]
        assert obs["id"] == esp["id"]
        assert obs["motivo"] == esp["motivo_esperado"]

    # 3. Verificar resumen.txt y reconciliación (suma_consolidado - aceptadas = 0)
    lineas_resumen = archivo_resum.read_text(encoding="utf-8").strip().splitlines()
    resumen_dict = {}
    for linea in lineas_resumen:
        if ":" in linea:
            k, v = linea.split(":", 1)
            resumen_dict[k.strip()] = int(v.strip())

    assert resumen_dict["leidas"] == 20
    assert resumen_dict["aceptadas"] == 15
    assert resumen_dict["rechazadas"] == 5
    assert resumen_dict["suma_consolidado"] == 15
    assert resumen_dict["diferencia_reconciliacion"] == 0
    assert resumen_dict["suma_consolidado"] - resumen_dict["aceptadas"] == 0


def test_reconciliacion_descuadre(tmp_path: Path):
    """PR-06 (R04): Si hay descuadre en reconciliación, retorna código 3."""
    consolidado_incompleto = [
        {"semana_iso": "2026-W43", "establecimiento": "CS Alameda", "distrito": "Cayma", "grupo_etario": "0-4", "casos": 1}
    ]
    rechazos = []
    # Total leídas 10, aceptadas 10, pero consolidado suma 1 -> descuadre
    codigo = exportar(consolidado_incompleto, rechazos, tmp_path, total_leidas=10)
    assert codigo == 3
