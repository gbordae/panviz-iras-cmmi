"""Módulo de filtrado contextual para Panviz IRAS (CR01)."""


def filtrar_por_distrito(
    validas: list[dict], distrito: str | None
) -> tuple[list[dict], int]:
    """Filtra la lista de registros válidos por nombre de distrito.

    Normalización:
        - Si distrito es None o cadena vacía, retorna todos los registros válidos.
        - Se aplica strip() y casefold() para comparar insensible a mayúsculas y espacios.
        - Los datos del registro original no se modifican.

    Retorna:
        (registros_filtrados, total_aceptadas_del_distrito)
    """
    if distrito is None:
        return validas, len(validas)

    distrito_norm = distrito.strip().casefold()
    if not distrito_norm:
        return validas, len(validas)

    filtrados = [
        r for r in validas if r["distrito"].strip().casefold() == distrito_norm
    ]
    return filtrados, len(filtrados)
