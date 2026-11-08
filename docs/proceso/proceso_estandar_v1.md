# Proceso Estándar v1.0 — Panviz IRAS

| Metadato  | Valor                        |
|-----------|------------------------------|
| Versión   | 1.0                          |
| Fecha     | 2026-11-08                   |
| Autor     | E1 Borda Espinoza, Gabriela  |
| Revisor   |                              |
| Estado    | borrador                     |

---

## Ciclo de desarrollo

### Etapa 1 — Requisitos

| Campo              | Contenido                                                                                      |
|--------------------|-----------------------------------------------------------------------------------------------|
| **Entradas**       | Enunciado del piloto, datos sintéticos de referencia, catálogo de datos                       |
| **Actividad**      | Elicitación, análisis y documentación de requisitos funcionales y reglas de calidad de datos  |
| **Responsable**    | E2 Meza Vizcarra, Cielo                                                                        |
| **Salida**         | `docs/requisitos/requisitos.md`, `docs/requisitos/catalogo_datos.md`, oráculos en `datos/`   |
| **Revisión**       | E3 Fernandez Huarca, Rodrigo revisa los requisitos de E2                                      |
| **Criterio cierre**| R01–R05 documentados con criterio de aceptación medible y oráculo definido antes de codificar |

---

### Etapa 2 — Planificación y riesgos

| Campo              | Contenido                                                                                      |
|--------------------|-----------------------------------------------------------------------------------------------|
| **Entradas**       | Requisitos aprobados, enunciado del piloto                                                    |
| **Actividad**      | Elaborar cronograma, asignar roles, identificar y registrar riesgos                           |
| **Responsable**    | E1 Borda Espinoza, Gabriela                                                                   |
| **Salida**         | `docs/gestion/cronograma.md`, `docs/gestion/equipo_roles.md`, `docs/gestion/riesgos.csv`     |
| **Revisión**       | E1 revisa el trabajo de E5 (configuración y medición)                                        |
| **Criterio cierre**| Cronograma con 7 fases asignadas; al menos 3 riesgos identificados con respuesta concreta     |

---

### Etapa 3 — Diseño

| Campo              | Contenido                                                                                      |
|--------------------|-----------------------------------------------------------------------------------------------|
| **Entradas**       | Requisitos R01–R05, oráculos, catálogo de datos                                               |
| **Actividad**      | Diseño de módulos, contratos de función (firma + pre/post), decisiones de diseño documentadas |
| **Responsable**    | E3 Fernandez Huarca, Rodrigo                                                                  |
| **Salida**         | Decisiones de diseño en `docs/proceso/`, módulos identificados en `src/`                     |
| **Revisión**       | E2 Meza Vizcarra, Cielo revisa que el diseño refleja los requisitos                           |
| **Criterio cierre**| Cada requisito R01–R04 tiene al menos un módulo o función asociada en `trazabilidad.csv`     |

---

### Etapa 4 — Construcción

| Campo              | Contenido                                                                                      |
|--------------------|-----------------------------------------------------------------------------------------------|
| **Entradas**       | Diseño aprobado, oráculos, proceso estándar v1                                                |
| **Actividad**      | Implementar módulos en `src/`; seguir convenciones de código (docstrings, tipos, constantes)  |
| **Responsable**    | E3 Fernandez Huarca, Rodrigo                                                                  |
| **Salida**         | Código fuente en `src/`, `requirements.txt` actualizado                                       |
| **Revisión**       | E4 Suclle Suca, Michael revisa el código de E3                                               |
| **Criterio cierre**| Todos los módulos importan sin error; sin `print` ni valores mágicos en producción           |

---

### Etapa 5 — Verificación

| Campo              | Contenido                                                                                      |
|--------------------|-----------------------------------------------------------------------------------------------|
| **Entradas**       | Código construido, oráculos, plantilla de pruebas                                             |
| **Actividad**      | Escribir y ejecutar pruebas unitarias en `tests/`; comparar resultados con oráculos           |
| **Responsable**    | E4 Suclle Suca, Michael                                                                       |
| **Salida**         | Pruebas en `tests/`, reporte `pytest -q`, evidencias en `evidencias/`                        |
| **Revisión**       | E1 Borda Espinoza audita el proceso de E4 (aseguramiento de calidad)                         |
| **Criterio cierre**| `pytest -q` sin fallos; cobertura de R01–R04; reporte guardado en `evidencias/`             |

---

### Etapa 6 — Validación

| Campo              | Contenido                                                                                      |
|--------------------|-----------------------------------------------------------------------------------------------|
| **Entradas**       | Sistema verificado, oráculos, plantilla de acta de validación                                 |
| **Actividad**      | Escenarios de validación con usuario simulado (E2); completar acta de validación              |
| **Responsable**    | E2 Meza Vizcarra, Cielo (usuario simulado); E4 Suclle Suca, Michael (ejecución)              |
| **Salida**         | Acta de validación en `evidencias/`                                                           |
| **Revisión**       | E1 Borda Espinoza revisa el acta de validación                                               |
| **Criterio cierre**| Todos los escenarios del acta con decisión "aceptado"; acta firmada por usuario simulado     |

---

### Etapa 7 — Liberación

| Campo              | Contenido                                                                                      |
|--------------------|-----------------------------------------------------------------------------------------------|
| **Entradas**       | Acta de validación cerrada, trazabilidad completa, `indice_evidencias.csv` actualizado        |
| **Actividad**      | Etiquetar versión en Git, actualizar `trazabilidad.csv`, cerrar tareas en tablero             |
| **Responsable**    | E5 Ccoscco Alvis, Italo                                                                       |
| **Salida**         | Etiqueta Git `v1.0`, baseline B1 documentado, `trazabilidad.csv` cerrado                     |
| **Revisión**       | E5 revisa la trazabilidad de cambios; E1 aprueba la liberación                               |
| **Criterio cierre**| Etiqueta existente en `git tag`; todos los requisitos con estado `implementado` en trazabilidad |

---

## Actividades transversales

### Gestión de configuración (CM)

- **Herramienta:** Git, rama única `main` durante el piloto.
- **Convención de commits:** `tipo: descripcion` (tipos: `chore`, `feat`, `fix`, `docs`, `test`).
- **Baselines:**

| Baseline | Evento que lo establece                  | Etiqueta Git | Aprobador | Fecha | Versión | Pendientes |
|----------|------------------------------------------|--------------|-----------|-------|---------|------------|
| B0       | Repositorio inicial con estructura y docs|              |           |       |         |            |
| B1       | Primera versión funcional verificada     |              |           |       |         |            |
| B2       | Versión con CR01 integrado y regresión   |              |           |       |         |            |

- **Ramas de cambio:** cuando se tramite CR01, se abre rama `cambio/CR01` y se fusiona con PR revisada.
- **Etiquetas:** `git tag -a v1.0 -m "Baseline B1"` al cierre de la etapa 7.

### Aseguramiento de calidad (QA)

- Cada entregable usa la `plantilla_revision.md` antes de pasar a la etapa siguiente.
- Las no conformidades se registran en `plantilla_no_conformidad.md` y se cierran antes de la liberación.
- E1 audita el proceso de E4 al menos una vez por iteración.

---

## Regla de cambios

| Paso | Responsable                   | Acción                                                                 |
|------|-------------------------------|------------------------------------------------------------------------|
| 1    | E2 Meza Vizcarra, Cielo       | Registra la solicitud de cambio (CR) en `registro_cambios.csv`        |
| 2    | E3 Fernandez Huarca, Rodrigo  | Estima el impacto en diseño y construcción; actualiza `trazabilidad.csv` |
| 3    | E4 Suclle Suca, Michael       | Define el plan de regresión (qué pruebas deben reejecutarse)           |
| 4    | E5 Ccoscco Alvis, Italo       | Identifica la versión afectada y la rama de cambio a abrir            |
| 5    | E1 Borda Espinoza, Gabriela   | Aprueba o rechaza con justificación documentada en `registro_cambios.csv` |

---

## Puntos de control B0 / B1 / B2

| Campo      | B0 | B1 | B2 |
|------------|----|----|-----|
| Aprobador  |    |    |     |
| Fecha      |    |    |     |
| Versión    |    |    |     |
| Pendientes |    |    |     |

