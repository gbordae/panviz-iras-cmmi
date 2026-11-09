"""Pruebas de consolidación y cálculo de semana ISO.

PR-05 (R03).
"""

import csv
import datetime
from pathlib import Path

from panviz.importador import importar
from panviz.validador import validar
from panviz.consolidador import consolidar, _semana_iso


def test_consolidacion_conocida():
    """PR-05 (R03): Ejecución sobre CSV sintético coincide con oraculo_consolidado.csv."""
    filas = importar(Path("datos/notificaciones_iras_sinteticas.csv"))
    validas, _ = validar(filas)
    consolidado = consolidar(validas)

    # Cargar oráculo sin codificar valores en duro
    with open("datos/oraculo_consolidado.csv", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        filas_oraculo = [
            {
                "semana_iso": r["semana_iso"],
                "establecimiento": r["establecimiento"],
                "distrito": r["distrito"],
                "grupo_etario": r["grupo_etario"],
                "casos": int(r["casos"]),
            }
            for r in reader
        ]

    assert len(consolidado) == 12
    assert len(consolidado) == len(filas_oraculo)
    assert sum(r["casos"] for r in consolidado) == 15

    # Comparación fila a fila, incluyendo orden exacto
    for i, (fila_obs, fila_esp) in enumerate(zip(consolidado, filas_oraculo)):
        assert fila_obs == fila_esp, f"Discrepancia en fila {i}: {fila_obs} != {fila_esp}"


def test_semana_iso_limite_anio():
    """PR-05 (R03): Cálculo de semana ISO en límites de año con isocalendar()."""
    d_fin_2026 = datetime.date(2026, 12, 31)
    iso_fin = d_fin_2026.isocalendar()
    esperado_fin = f"{iso_fin[0]}-W{iso_fin[1]:02d}"
    assert _semana_iso(d_fin_2026) == esperado_fin

    d_ini_2027 = datetime.date(2027, 1, 1)
    iso_ini = d_ini_2027.isocalendar()
    esperado_ini = f"{iso_ini[0]}-W{iso_ini[1]:02d}"
    assert _semana_iso(d_ini_2027) == esperado_ini
