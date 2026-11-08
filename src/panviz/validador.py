"""Valida cada fila según las reglas del catálogo de datos (proceso_estandar v1.0)."""

import datetime

CAMPOS_OBLIGATORIOS = [
    "id",
    "fecha_notificacion",
    "establecimiento",
    "distrito",
    "grupo_etario",
    "evento",
]
GRUPOS_VALIDOS = {"0-4", "5-14", "15-59", "60+"}
EVENTO_VALIDO = "IRAS"


def _fecha_valida(valor: str) -> bool:
    """Retorna True si valor es una fecha calendario existente en formato YYYY-MM-DD."""
    try:
        datetime.date.fromisoformat(valor)
        return True
    except ValueError:
        return False


def validar(filas: list[dict[str, str]]) -> tuple[list[dict], list[dict]]:
    """Valida las filas y retorna (registros_validos, rechazos).

    Orden de evaluación por fila:
        1. Campo obligatorio vacío
        2. Fecha imposible o formato incorrecto
        3. Evento distinto de IRAS
        4. Grupo etario fuera del catálogo
        5. Clave duplicada (se acepta la primera aparición)

    registros_validos: lista de dicts con campos parseados; fecha como datetime.date.
    rechazos: lista de dicts con fila_datos (int, 1-based), id (str), motivo (str).
    """
    validas: list[dict] = []
    rechazos: list[dict] = []
    ids_vistos: dict[str, int] = {}

    for idx, fila in enumerate(filas, start=1):
        # 1. Campos obligatorios vacíos
        campo_vacio = None
        for campo in CAMPOS_OBLIGATORIOS:
            if not fila.get(campo, "").strip():
                campo_vacio = campo
                break
        if campo_vacio:
            rechazos.append({
                "fila_datos": idx,
                "id": fila.get("id", "").strip(),
                "motivo": f"campo obligatorio vacio ({campo_vacio})",
            })
            continue

        # 2. Fecha imposible o formato incorrecto
        fecha_str = fila["fecha_notificacion"].strip()
        if not _fecha_valida(fecha_str):
            rechazos.append({
                "fila_datos": idx,
                "id": fila["id"].strip(),
                "motivo": "fecha imposible",
            })
            continue

        # 3. Evento distinto de IRAS
        evento = fila["evento"].strip()
        if evento != EVENTO_VALIDO:
            rechazos.append({
                "fila_datos": idx,
                "id": fila["id"].strip(),
                "motivo": "evento distinto de IRAS",
            })
            continue

        # 4. Grupo etario fuera del catálogo
        grupo = fila["grupo_etario"].strip()
        if grupo not in GRUPOS_VALIDOS:
            rechazos.append({
                "fila_datos": idx,
                "id": fila["id"].strip(),
                "motivo": "grupo etario fuera de catalogo",
            })
            continue

        # 5. Clave duplicada
        fila_id = fila["id"].strip()
        if fila_id in ids_vistos:
            rechazos.append({
                "fila_datos": idx,
                "id": fila_id,
                "motivo": "clave duplicada",
            })
            continue

        ids_vistos[fila_id] = idx
        validas.append({
            "fila_datos": idx,
            "id": fila_id,
            "fecha": datetime.date.fromisoformat(fecha_str),
            "establecimiento": fila["establecimiento"].strip(),
            "distrito": fila["distrito"].strip(),
            "grupo_etario": grupo,
            "evento": evento,
        })

    return validas, rechazos

