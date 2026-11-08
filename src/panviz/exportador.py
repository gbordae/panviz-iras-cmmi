"""Escribe los archivos de salida y ejecuta la reconciliación."""

import csv
from pathlib import Path


def exportar(
    consolidado: list[dict],
    rechazos: list[dict],
    ruta_salida: Path,
    total_leidas: int,
) -> int:
    """Escribe consolidado.csv, rechazos.csv y resumen.txt en ruta_salida.

    Reconciliación: suma(casos en consolidado) - filas_aceptadas debe ser 0.
    Retorna 0 si OK, 3 si la diferencia es distinta de cero.
    """
    ruta_salida.mkdir(parents=True, exist_ok=True)

    # consolidado.csv
    with open(ruta_salida / "consolidado.csv", "w", encoding="utf-8", newline="") as f:
        campos = ["semana_iso", "establecimiento", "distrito", "grupo_etario", "casos"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(consolidado)

    # rechazos.csv
    with open(ruta_salida / "rechazos.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["fila_datos", "id", "motivo"])
        writer.writeheader()
        writer.writerows(rechazos)

    total_rechazadas = len(rechazos)
    total_aceptadas = total_leidas - total_rechazadas
    suma_consolidado = sum(r["casos"] for r in consolidado)
    diferencia = suma_consolidado - total_aceptadas
    codigo_salida = 0 if diferencia == 0 else 3

    # resumen.txt
    with open(ruta_salida / "resumen.txt", "w", encoding="utf-8") as f:
        f.write(f"leidas: {total_leidas}\n")
        f.write(f"aceptadas: {total_aceptadas}\n")
        f.write(f"rechazadas: {total_rechazadas}\n")
        f.write(f"suma_consolidado: {suma_consolidado}\n")
        f.write(f"diferencia_reconciliacion: {diferencia}\n")
        if diferencia != 0:
            f.write(
                f"ADVERTENCIA: diferencia de reconciliacion = {diferencia}."
                f" Codigo de salida: {codigo_salida}\n"
            )

    return codigo_salida

