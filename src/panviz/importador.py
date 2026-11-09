"""Lee el CSV de entrada y verifica el contrato de encabezado."""

import csv
from pathlib import Path

ENCABEZADO_ESPERADO = [
    "id",
    "fecha_notificacion",
    "establecimiento",
    "distrito",
    "grupo_etario",
    "evento",
]


def importar(ruta: Path) -> list[dict[str, str]]:
    """Lee el CSV y verifica el contrato de encabezado.

    Retorna una lista de dicts (campo -> valor en texto) con todas las filas.
    Lanza SystemExit(2) si el encabezado no coincide exactamente con el contrato.
    """
    with open(ruta, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        encabezado = list(reader.fieldnames or [])
        if encabezado != ENCABEZADO_ESPERADO:
            print(
                f"ERROR: encabezado inválido.\n"
                f"  Esperado : {ENCABEZADO_ESPERADO}\n"
                f"  Encontrado: {encabezado}"
            )
            raise SystemExit(2)
        return list(reader)

