# Plantilla para Módulo Nuevo de Panviz

> **Propósito:** Guía reutilizable para incorporar un nuevo módulo al sistema Panviz
> siguiendo el proceso estándar v1.0 y la regla de adaptación.
> **No construir el módulo con esta plantilla:** es un punto de partida documental.

---

## 1. Identificar el tipo de módulo

Consultar `docs/proceso/regla_adaptacion.md` y determinar:

- [ ] Caso A — Importación CSV
- [ ] Caso B — Entrada por formulario
- [ ] Otro (describir y documentar la adaptación)

## 2. Definir requisitos del módulo

Completar una instancia de `plantilla_requisito.md` por cada requisito.
Registrar en `docs/requisitos/requisitos.md` y en `trazabilidad.csv`.

## 3. Definir el oráculo antes de codificar

- Crear `datos/oraculo_<modulo>_rechazos.csv`
- Crear `datos/oraculo_<modulo>_consolidado.csv` (si aplica)
- Verificar el oráculo con un script temporal (no en `src/`)

## 4. Registrar en el tablero y en el índice de evidencias

- Agregar tarea en `docs/gestion/tablero_tareas.csv`
- Agregar evidencias en `evidencias/indice_evidencias.csv`

## 5. Aplicar el ciclo de desarrollo

Seguir las 7 etapas del proceso estándar v1.0:

| Etapa | Acción mínima para este módulo |
|-------|-------------------------------|
| Requisitos      | Completar `plantilla_requisito.md`         |
| Planificación   | Actualizar `cronograma.md` y `riesgos.csv` |
| Diseño          | Documentar decisiones de diseño            |
| Construcción    | Implementar en `src/<modulo>/`             |
| Verificación    | Pruebas en `tests/test_<modulo>.py`        |
| Validación      | Completar `plantilla_acta_validacion.md`   |
| Liberación      | Etiquetar versión y cerrar trazabilidad    |

## 6. Gestión de cambios

Si el módulo introduce un cambio sobre funciones existentes, tramitar un CR según la
regla de cambios del proceso estándar v1.0 (`plantilla_cambio.md`).

## 7. Criterio de incorporación completada

- [ ] Todos los requisitos del módulo en estado `implementado` en `trazabilidad.csv`
- [ ] Pruebas `pytest -q` sin fallos
- [ ] Acta de validación cerrada
- [ ] Evidencias registradas en `indice_evidencias.csv`
- [ ] Etiqueta Git creada
