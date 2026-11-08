"""Pruebas unitarias de reglas de validación.

PR-02, PR-03, PR-04 (R02).
"""

from panviz.validador import validar


def test_validacion_campo_obligatorio_vacio():
    """PR-02 (R02): Rechazo por campo obligatorio vacío (motivo exacto)."""
    filas = [
        {
            "id": "T001",
            "fecha_notificacion": "2026-10-29",
            "establecimiento": "",
            "distrito": "Yanahuara",
            "grupo_etario": "0-4",
            "evento": "IRAS",
        }
    ]
    validas, rechazos = validar(filas)
    assert len(validas) == 0
    assert len(rechazos) == 1
    assert rechazos[0]["fila_datos"] == 1
    assert rechazos[0]["id"] == "T001"
    assert rechazos[0]["motivo"] == "campo obligatorio vacio (establecimiento)"


def test_validacion_evento_distinto_iras():
    """PR-02 (R02): Rechazo por evento distinto de IRAS con motivo exacto."""
    filas = [
        {
            "id": "T002",
            "fecha_notificacion": "2026-11-03",
            "establecimiento": "Hospital Base",
            "distrito": "Cercado",
            "grupo_etario": "5-14",
            "evento": "COVID",
        }
    ]
    validas, rechazos = validar(filas)
    assert len(validas) == 0
    assert len(rechazos) == 1
    assert rechazos[0]["motivo"] == "evento distinto de IRAS"


def test_validacion_grupo_etario_fuera_catalogo():
    """PR-02 (R02): Rechazo por grupo etario fuera de catálogo con motivo exacto."""
    filas = [
        {
            "id": "T003",
            "fecha_notificacion": "2026-11-04",
            "establecimiento": "CS Mirador",
            "distrito": "Yanahuara",
            "grupo_etario": "90+",
            "evento": "IRAS",
        }
    ]
    validas, rechazos = validar(filas)
    assert len(validas) == 0
    assert len(rechazos) == 1
    assert rechazos[0]["motivo"] == "grupo etario fuera de catalogo"


def test_validacion_fecha_imposible():
    """PR-03 (R02): Rechazo de 2026-02-30 y formato no YYYY-MM-DD."""
    filas = [
        {
            "id": "T004",
            "fecha_notificacion": "2026-02-30",
            "establecimiento": "CS Alameda",
            "distrito": "Cayma",
            "grupo_etario": "15-59",
            "evento": "IRAS",
        },
        {
            "id": "T005",
            "fecha_notificacion": "30/10/2026",
            "establecimiento": "CS Alameda",
            "distrito": "Cayma",
            "grupo_etario": "15-59",
            "evento": "IRAS",
        },
    ]
    validas, rechazos = validar(filas)
    assert len(validas) == 0
    assert len(rechazos) == 2
    assert rechazos[0]["fila_datos"] == 1
    assert rechazos[0]["motivo"] == "fecha imposible"
    assert rechazos[1]["fila_datos"] == 2
    assert rechazos[1]["motivo"] == "fecha imposible"


def test_validacion_clave_duplicada():
    """PR-04 (R02): Se acepta la primera aparición del id y se rechazan las siguientes."""
    filas = [
        {
            "id": "N007",
            "fecha_notificacion": "2026-10-27",
            "establecimiento": "CS Alameda",
            "distrito": "Cayma",
            "grupo_etario": "0-4",
            "evento": "IRAS",
        },
        {
            "id": "N007",
            "fecha_notificacion": "2026-10-28",
            "establecimiento": "CS Alameda",
            "distrito": "Cayma",
            "grupo_etario": "5-14",
            "evento": "IRAS",
        },
    ]
    validas, rechazos = validar(filas)
    assert len(validas) == 1
    assert validas[0]["id"] == "N007"
    assert validas[0]["fila_datos"] == 1
    assert len(rechazos) == 1
    assert rechazos[0]["fila_datos"] == 2
    assert rechazos[0]["id"] == "N007"
    assert rechazos[0]["motivo"] == "clave duplicada"
