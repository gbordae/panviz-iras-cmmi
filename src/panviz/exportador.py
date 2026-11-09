"""Escribe los archivos de salida y ejecuta la reconciliación."""

import csv
from pathlib import Path


def exportar(
    consolidado: list[dict],
    rechazos: list[dict],
    ruta_salida: Path,
    total_leidas: int,
    distrito_filtrado: str | None = None,
    aceptadas_del_distrito: int | None = None,
) -> int:
    """Escribe consolidado.csv, rechazos.csv y resumen.txt en ruta_salida.

    Reconciliación:
        - Si hay filtro activo: suma(casos consolidado) - aceptadas_del_distrito.
        - Sin filtro: suma(casos consolidado) - total_aceptadas.
        - Retorna 0 si la diferencia es 0; retorna 3 si es distinta de cero.
    """
    ruta_salida.mkdir(parents=True, exist_ok=True)

    # consolidado.csv
    with open(
        ruta_salida / "consolidado.csv", "w", encoding="utf-8", newline=""
    ) as f:
        campos = [
            "semana_iso",
            "establecimiento",
            "distrito",
            "grupo_etario",
            "casos",
        ]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(consolidado)

    # rechazos.csv
    with open(
        ruta_salida / "rechazos.csv", "w", encoding="utf-8", newline=""
    ) as f:
        writer = csv.DictWriter(f, fieldnames=["fila_datos", "id", "motivo"])
        writer.writeheader()
        writer.writerows(rechazos)

    total_rechazadas = len(rechazos)
    total_aceptadas = total_leidas - total_rechazadas
    suma_consolidado = sum(r["casos"] for r in consolidado)

    # Reconciliación contextual
    hay_filtro = distrito_filtrado is not None and distrito_filtrado.strip() != ""
    if hay_filtro:
        esperado_comparacion = (
            aceptadas_del_distrito
            if aceptadas_del_distrito is not None
            else total_aceptadas
        )
    else:
        esperado_comparacion = total_aceptadas

    diferencia = suma_consolidado - esperado_comparacion
    codigo_salida = 0 if diferencia == 0 else 3

    # resumen.txt
    with open(ruta_salida / "resumen.txt", "w", encoding="utf-8") as f:
        f.write(f"leidas: {total_leidas}\n")
        f.write(f"aceptadas: {total_aceptadas}\n")
        f.write(f"rechazadas: {total_rechazadas}\n")
        if hay_filtro:
            f.write(f"distrito_filtrado: {distrito_filtrado.strip()}\n")
            f.write(f"aceptadas_del_distrito: {aceptadas_del_distrito}\n")
        f.write(f"suma_consolidado: {suma_consolidado}\n")
        f.write(f"diferencia_reconciliacion: {diferencia}\n")
        if hay_filtro and aceptadas_del_distrito == 0:
            f.write(
                f"AVISO: el distrito '{distrito_filtrado.strip()}' no presenta registros aceptados.\n"
            )
        if diferencia != 0:
            f.write(
                f"ADVERTENCIA: diferencia de reconciliacion = {diferencia}. "
                f"Codigo de salida: {codigo_salida}\n"
            )

    return codigo_salida
