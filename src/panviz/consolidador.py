"""Consolida registros válidos por semana ISO, establecimiento, distrito y grupo etario."""

import datetime


def _semana_iso(fecha: datetime.date) -> str:
    """Formatea la semana ISO como 'AAAA-Wss' usando el año ISO."""
    iso = fecha.isocalendar()   # (año_iso, semana, dia_semana)
    return f"{iso[0]}-W{iso[1]:02d}"


def consolidar(validas: list[dict]) -> list[dict]:
    """Agrupa registros válidos y cuenta casos por grupo.

    Orden de salida:
        - Primero por semana_iso (lexicográfico ascendente).
        - Dentro de cada semana, por orden de primera aparición en el archivo.

    Retorna lista de dicts con:
        semana_iso, establecimiento, distrito, grupo_etario, casos.
    """
    conteo: dict[tuple, int] = {}
    indice_primera: dict[tuple, int] = {}

    for r in validas:
        sem = _semana_iso(r["fecha"])
        clave = (sem, r["establecimiento"], r["distrito"], r["grupo_etario"])
        if clave not in conteo:
            conteo[clave] = 0
            indice_primera[clave] = len(indice_primera)
        conteo[clave] += 1

    claves_ordenadas = sorted(
        conteo.keys(),
        key=lambda c: (c[0], indice_primera[c]),
    )

    return [
        {
            "semana_iso": sem,
            "establecimiento": est,
            "distrito": dis,
            "grupo_etario": grp,
            "casos": conteo[(sem, est, dis, grp)],
        }
        for sem, est, dis, grp in claves_ordenadas
    ]

