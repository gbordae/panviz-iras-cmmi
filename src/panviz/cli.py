"""Interfaz de línea de comandos de Panviz IRAS."""

import argparse
import sys
from pathlib import Path

from .exportador import exportar
from .consolidador import consolidar
from .validador import validar
from .importador import importar


def main() -> None:
    """Parsea argumentos y orquesta el pipeline completo.

    Uso:
        $env:PYTHONPATH = "src"
        python -m panviz --entrada <csv> --salida <carpeta>

    Códigos de salida:
        0  — OK; reconciliación correcta.
        2  — Encabezado del CSV no cumple el contrato.
        3  — Diferencia de reconciliación distinta de cero.
    """
    parser = argparse.ArgumentParser(
        prog="panviz",
        description="Panviz IRAS — importación, validación y consolidación de notificaciones.",
    )
    parser.add_argument(
        "--entrada",
        required=True,
        type=Path,
        metavar="CSV",
        help="Ruta al CSV de entrada.",
    )
    parser.add_argument(
        "--salida",
        required=True,
        type=Path,
        metavar="CARPETA",
        help="Carpeta de salida para los archivos generados.",
    )
    args = parser.parse_args()

    filas = importar(args.entrada)           # SystemExit(2) si contrato falla
    validas, rechazos = validar(filas)
    consolidado = consolidar(validas)
    codigo = exportar(consolidado, rechazos, args.salida, total_leidas=len(filas))

    print(f"Panviz: procesadas {len(filas)} filas — "
          f"aceptadas {len(validas)}, rechazadas {len(rechazos)}.")

    if codigo != 0:
        print(f"ERROR: reconciliación fallida (código {codigo}).", file=sys.stderr)
        sys.exit(codigo)

