"""Pruebas de importación y contrato de columnas.

PR-01 (R01): Importación válida y prueba de contrato de columnas.
"""

from pathlib import Path
import pytest

from panviz.importador import importar


def test_importacion_valida():
    """PR-01 (R01): El CSV sintético se lee con exactamente 20 filas de datos."""
    ruta_csv = Path("datos/notificaciones_iras_sinteticas.csv")
    filas = importar(ruta_csv)
    assert len(filas) == 20
    assert filas[0]["id"] == "N001"
    assert filas[-1]["id"] == "N015"


def test_importacion_contrato_columnas_invalido(tmp_path: Path):
    """PR-01 (R01): CSV con encabezado distinto o en otro orden termina con salida 2."""
    csv_desordenado = tmp_path / "encabezado_alterado.csv"
    # Encabezado en orden incorrecto
    contenido = (
        "id,establecimiento,fecha_notificacion,distrito,grupo_etario,evento\n"
        "N001,CS Alameda,2026-10-20,Cayma,0-4,IRAS\n"
    )
    csv_desordenado.write_text(contenido, encoding="utf-8")

    with pytest.raises(SystemExit) as exc_info:
        importar(csv_desordenado)
    assert exc_info.value.code == 2


def test_importacion_contrato_columnas_faltantes(tmp_path: Path):
    """PR-01 (R01): CSV con columnas faltantes termina con código de salida 2."""
    csv_incompleto = tmp_path / "incompleto.csv"
    contenido = (
        "id,fecha_notificacion,establecimiento\n"
        "N001,2026-10-20,CS Alameda\n"
    )
    csv_incompleto.write_text(contenido, encoding="utf-8")

    with pytest.raises(SystemExit) as exc_info:
        importar(csv_incompleto)
    assert exc_info.value.code == 2
