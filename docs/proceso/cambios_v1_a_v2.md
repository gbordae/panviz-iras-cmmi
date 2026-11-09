# Registro de Cambios del Proceso Estándar: v1.0 a v2.0 — Panviz IRAS

> **Aclaración metodológica:** El Proceso Estándar v1.0 (`docs/proceso/proceso_estandar_v1.md`) y sus plantillas asociadas se conservan inalteradas en el repositorio para permitir la trazabilidad histórica y la comparación de la evolución del proceso.
> El Proceso Estándar v2.0 y sus plantillas v2 representan una **propuesta de mejora continua institucionalizada**, pendiente de aprobación formal definitiva por E1/E4.

---

## Tabla de Cambios: v1.0 a v2.0

| N° | Cambio introducido | Origen de la lección | Artefacto modificado / creado | Estado |
|:--:|:-------------------|:--------------------:|:------------------------------|:------:|
| 1 | Ejecución obligatoria con el Python del entorno virtual (`.\.venv\Scripts\python.exe`), registro de `sys.prefix` en toda evidencia de prueba, y validación de `requirements.txt` en UTF-8 sin BOM e instalable en limpio antes de cerrar B1. | **NC-01** (desfase de versión pytest y BOM en requirements.txt) | `docs/proceso/proceso_estandar_v2.md`<br>`docs/proceso/plantillas/plantilla_pruebas_v2.md` | propuesto - pendiente de aprobacion E1/E4 |
| 2 | Obligatoriedad de declarar el comportamiento ante error en cada requisito (códigos de salida específicos como 2 o 3, y mensajes por stderr). | **H-01** (R04 no definía qué pasaba si la reconciliación fallaba) | `docs/proceso/proceso_estandar_v2.md`<br>`docs/proceso/plantillas/plantilla_requisito_v2.md` | propuesto - pendiente de aprobacion E1/E4 |
| 3 | Obligatoriedad de declarar reglas de normalización de texto (insensibilidad a mayúsculas/minúsculas y recorte de espacios) en requisitos y solicitudes de cambio que comparen cadenas. | **H-02** (distrito se comparaba por texto exacto sin prever mayúsculas) | `docs/proceso/proceso_estandar_v2.md`<br>`docs/proceso/plantillas/plantilla_requisito_v2.md`<br>`docs/proceso/plantillas/plantilla_cambio_v2.md` | propuesto - pendiente de aprobacion E1/E4 |
| 4 | Comprobación explícita de no contradicción y consistencia entre criterios de aceptación antes de la aprobación de un CR (resolviendo colisiones entre paridad sin filtro y campos nuevos en resumen). | **Revisión de CR01** (conflicto resuelto por aclaración de E1) | `docs/proceso/proceso_estandar_v2.md`<br>`docs/proceso/plantillas/plantilla_cambio_v2.md` | propuesto - pendiente de aprobacion E1/E4 |
| 5 | Archivado formal de evidencias de revisión con autor y hora reales en `evidencias/revisiones/` con indexación obligatoria; y delimitación de que toda aprobación por pares cubre estrictamente el commit revisado, exigiendo nueva revisión ante cambios posteriores. | **PR y revisiones** (aprobación en GitHub de código v0 previo a CR01) | `docs/proceso/proceso_estandar_v2.md` | propuesto - pendiente de aprobacion E1/E4 |
