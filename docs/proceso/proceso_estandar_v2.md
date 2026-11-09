# Proceso Estándar v2.0 — Panviz IRAS

| Metadato  | Valor                                                          |
|-----------|----------------------------------------------------------------|
| Versión   | 2.0                                                            |
| Fecha     | 2026-11-08                                                     |
| Autor     | E1 Borda Espinoza, Gabriela (Coordinación y mejora)            |
| Revisor   |                                                                |
| Estado    | borrador - pendiente de revision de E4 y aprobacion de E1       |

> **Nota de versión:** Esta versión 2.0 incorpora mejoras derivadas de la experiencia real del piloto (No Conformidad NC-01, hallazgos H-01 y H-02 en requisitos, refinamiento de CR01 y revisión por pares en GitHub). La versión 1.0 se mantiene inalterada en `docs/proceso/proceso_estandar_v1.md` como línea base histórica de comparación.

---

## Ciclo de desarrollo (v2.0)

### Etapa 1 — Requisitos (Mejorada)

| Campo              | Contenido                                                                                      |
|--------------------|-----------------------------------------------------------------------------------------------|
| **Entradas**       | Enunciado del piloto, datos sintéticos de referencia, catálogo de datos, lecciones de diseño  |
| **Actividad**      | Elicitación, análisis y especificación de requisitos funcionales y reglas de calidad. **Mejora v2:** Cada requisito debe declarar explícitamente su comportamiento ante error (código de salida y mensaje; *origen H-01*) y, en todo criterio que compare texto, debe especificarse la política de normalización de mayúsculas y espacios (*origen H-02*). |
| **Responsable**    | E2 Meza Vizcarra, Cielo                                                                        |
| **Salida**         | `docs/requisitos/requisitos.md` (v0.2+), `docs/requisitos/catalogo_datos.md`, oráculos en `datos/` |
| **Revisión**       | E3 Fernandez Huarca, Rodrigo revisa los requisitos de E2 (verificando completitud ante fallos) |
| **Criterio cierre**| R01–R05 y cambios documentados con criterios de aceptación medibles, códigos de terminación ante error definidos y reglas de normalización declaradas |

---

### Etapa 2 — Planificación y riesgos

| Campo              | Contenido                                                                                      |
|--------------------|-----------------------------------------------------------------------------------------------|
| **Entradas**       | Requisitos aprobados, enunciado del piloto                                                    |
| **Actividad**      | Elaborar cronograma, asignar roles, identificar y registrar riesgos en matriz                 |
| **Responsable**    | E1 Borda Espinoza, Gabriela                                                                   |
| **Salida**         | `docs/gestion/cronograma.md`, `docs/gestion/equipo_roles.md`, `docs/gestion/riesgos.csv`     |
| **Revisión**       | E1 revisa el trabajo de E5 (configuración y medición)                                        |
| **Criterio cierre**| Cronograma con 7 fases asignadas; riesgos documentados con plan de respuesta y disparadores    |

---

### Etapa 3 — Diseño (Mejorada)

| Campo              | Contenido                                                                                      |
|--------------------|-----------------------------------------------------------------------------------------------|
| **Entradas**       | Requisitos con especificación de error y normalización, oráculos                              |
| **Actividad**      | Diseño de módulos, contratos de interfaces (pre/post), funciones puras para consolidación y filtros |
| **Responsable**    | E3 Fernandez Huarca, Rodrigo                                                                  |
| **Salida**         | `docs/requisitos/diseno.md` con firmas de funciones, contratos de CLI y manejo de errores    |
| **Revisión**       | E2 revisa que el diseño refleje los requisitos y E4 revisa la verificabilidad                 |
| **Criterio cierre**| Módulos trazados en `trazabilidad.csv`, contratos de columnas y códigos de error formalizados |

---

### Etapa 4 — Construcción (Mejorada)

| Campo              | Contenido                                                                                      |
|--------------------|-----------------------------------------------------------------------------------------------|
| **Entradas**       | Diseño aprobado, oráculos congelados, entorno virtual configurado                             |
| **Actividad**      | Implementación de código en `src/`. **Mejora v2 mandatoria:** Todo comando de construcción y verificación se ejecuta exclusivamente mediante el intérprete del entorno virtual (`.\.venv\Scripts\python.exe`). Antes de cerrar B1, se valida obligatoriamente que `requirements.txt` esté codificado en UTF-8 sin BOM y sea instalable limpiamente en un venv sin dependencias externas (*origen NC-01*). |
| **Responsable**    | E3 Fernandez Huarca, Rodrigo                                                                  |
| **Salida**         | Código fuente en `src/panviz/`, `requirements.txt` en UTF-8 sin BOM verificado               |
| **Revisión**       | E4 Suclle Suca, Michael revisa el código de E3                                               |
| **Criterio cierre**| Módulos importables sin errores; cero valores mágicos del oráculo en duro; código documentado |

---

### Etapa 5 — Verificación (Mejorada)

| Campo              | Contenido                                                                                      |
|--------------------|-----------------------------------------------------------------------------------------------|
| **Entradas**       | Código construido, oráculos en `datos/`, plan de pruebas                                      |
| **Actividad**      | Ejecución automatizada de pruebas con `pytest`. **Mejora v2 mandatoria:** Toda evidencia de prueba debe registrar explícitamente en su cabecera la fecha real, el intérprete Python y el valor de `sys.prefix` para garantizar que no se utilizó el Python global (*origen NC-01*). |
| **Responsable**    | E4 Suclle Suca, Michael                                                                       |
| **Salida**         | Pruebas en `tests/`, reportes en `evidencias/pruebas/` con cabecera de entorno trazable       |
| **Revisión**       | E1 Borda Espinoza audita el proceso de pruebas y la integridad del entorno                   |
| **Criterio cierre**| 100% pruebas aprobadas en pytest; evidencia con `sys.prefix` del venv archivada               |

---

### Etapa 6 — Validación

| Campo              | Contenido                                                                                      |
|--------------------|-----------------------------------------------------------------------------------------------|
| **Entradas**       | Sistema verificado, oráculos, plantilla de acta de validación                                 |
| **Actividad**      | Ejecución de escenarios de validación con usuario simulado (E2); acta de validación            |
| **Responsable**    | E2 Meza Vizcarra, Cielo (usuario simulado); E4 Suclle Suca, Michael (ejecución técnica)        |
| **Salida**         | Acta de validación en `evidencias/`                                                           |
| **Revisión**       | E1 Borda Espinoza revisa el acta de validación                                               |
| **Criterio cierre**| Escenarios aceptados por usuario simulado; nota de no aval clínico/sanitario preservada       |

---

### Etapa 7 — Liberación y Cierre de Línea Base

| Campo              | Contenido                                                                                      |
|--------------------|-----------------------------------------------------------------------------------------------|
| **Entradas**       | Validación aprobada, trazabilidad bidireccional completa, índice de evidencias al día         |
| **Actividad**      | Etiquetar versión en Git, cerrar tareas en tablero, establecer baselines                      |
| **Responsable**    | E5 Ccoscco Alvis, Italo                                                                       |
| **Salida**         | Etiqueta Git correspondiente, baseline documentado en seguimiento PMC                         |
| **Revisión**       | E5 revisa la trazabilidad de cambios; E1 aprueba la liberación formal                        |
| **Criterio cierre**| Etiqueta creada; todos los requisitos en estado verificado/aprobado en trazabilidad           |

---

## Actividades transversales y aseguramiento de calidad (v2.0)

### Gestión de configuración y evidencias de revisión (*Mejora v2: origen PR y revisiones*)
- Toda evidencia de revisión (mensajes de chat, revisiones de Pull Request) se archiva como captura o registro con hora y autor reales en `evidencias/revisiones/` y se indexa en `evidencias/indice_evidencias.csv`.
- **Regla de alcance de aprobación:** Si un producto cambia después de haber sido revisado y aprobado por pares, se debe registrar explícitamente que la aprobación previa cubre únicamente el commit evaluado (p. ej. código v0 en PR), y se debe tramitar una nueva revisión técnica para los cambios incrementales posteriores.

---

## Regla de cambios — Gestión de CR (v2.0)

| Paso | Responsable                   | Acción                                                                 |
|------|-------------------------------|------------------------------------------------------------------------|
| 1    | E2 Meza Vizcarra, Cielo       | Registra la solicitud de cambio (CR) en `registro_cambios.csv`. **Mejora v2:** Si el cambio involucra comparaciones de texto, define la normalización requerida (*origen H-02*). |
| 2    | E3 Fernandez Huarca, Rodrigo  | Estima el impacto en diseño y código; actualiza `trazabilidad.csv` y deja constancia documental. |
| 3    | E4 Suclle Suca, Michael       | Define el plan de regresión y los nuevos casos de prueba (PR-xx).     |
| 4    | E5 Ccoscco Alvis, Italo       | Identifica la versión afectada exacta en Git y verifica que no sea previa a correcciones críticas de entorno (*origen NC-01*). |
| 5    | E1 Borda Espinoza, Gabriela   | **Mejora v2:** Antes de aprobar, el solicitante y E1 comprueban que los criterios de aceptación no se contradigan entre sí ni con la línea base vigente (*origen revisión de CR01*); luego aprueba o rechaza con justificación técnica. |

---

## Puntos de control B0 / B1 / B2

| Campo      | B0 | B1 | B2 |
|------------|----|----|-----|
| Aprobador  |    |    |     |
| Fecha      |    |    |     |
| Versión    |    |    |     |
| Pendientes |    |    |     |
