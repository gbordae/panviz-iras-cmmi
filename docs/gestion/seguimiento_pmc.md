# Seguimiento y Control del Proyecto (PMC) — Piloto Panviz IRAS

| Metadato  | Valor                                              |
|-----------|----------------------------------------------------|
| Autor     | E1 Borda Espinoza, Gabriela (Coordinación y mejora)|
| Proceso   | CMMI-DEV v1.3 — Nivel 2: Project Monitoring and Control (PMC) |

---

## Corte 1 — 2026-11-08 16:34:32

### 1. Estado de Tareas del Tablero (`docs/gestion/tablero_tareas.csv`)

| ID  | Tarea | Responsable | Estado | Fecha creación | Fecha cierre | Evidencia |
|:---:|:------|:------------|:------:|:--------------:|:------------:|:----------|
| T01 | Estructura y entorno | E5 Ccoscco Alvis Italo | **cerrado** | 2026-11-08 | 2026-11-08 | `evidencias/entorno.txt` |
| T02 | Requisitos datos y oraculo | E2 Meza Vizcarra Cielo | **en revision** | 2026-11-08 | | |
| T03 | Proceso estandar v1 plantillas formacion y riesgos | E1 Borda Espinoza Gabriela | **en revision** | 2026-11-08 | | |
| T04 | Diseno DAR y componente | E3 Fernandez Huarca Rodrigo | **en revision** | 2026-11-08 | | |
| T05 | Pruebas y preparacion de revision | E4 Suclle Suca Michael | **en revision** | 2026-11-08 | | |
| T06 | NC-01 y registro de CR01 | E1 Borda Espinoza Gabriela | **en revision** | 2026-11-08 | | |

---

### 2. Indicadores del Proyecto en el Corte 1

Tomados de la medición objetiva en `evidencias/medicion/indicadores_corte1.txt`:

1. **Trazabilidad de requisitos:** 4/6 (66.67%) — R01 a R04 con diseño, código y pruebas; R05 y CR01 pendientes.
2. **Pruebas satisfactorias:** 12/12 (100.00%) — 12 funciones pytest pasadas en entorno virtual, cubriendo PR-01 a PR-06.
3. **Detección de errores de datos:** 5/5 (100.00%) — 5 filas rechazadas con motivos exactos según el oráculo predefinido.
4. **Reconciliación de casos:** 15 − 15 = 0 casos de discrepancia (cuadre matemático exacto).
5. **Eficacia de formación:** 0/5 (0.00%) — Sesión y comprobaciones documentadas pero aún no ejecutadas por el equipo.
6. **Cumplimiento de revisiones por pares:** 0/3 (0.00%) — Checklists estructurados pero firmas/revisiones pendientes de ejecución.

---

### 3. Desviaciones Detectadas y Acciones Correctivas

#### Desviación NC-01: Desfase de entorno entre evidencia de pruebas y requirements.txt
- **Descripción:** La evidencia preliminar `pytest_v0.txt` reportó `pytest 9.1.1` (ejecutado con Python global) mientras que `.venv` contenía `pytest 9.2.0`; además `requirements.txt` poseía codificación UTF-16 LE con BOM generada por redirección PowerShell.
- **Acción tomada:**
  1. Diagnóstico causal documentado en `evidencias/nc01_analisis.md`.
  2. Regeneración de `requirements.txt` en UTF-8 sin BOM con fin de línea LF.
  3. Verificación preliminar en entorno limpio temporal `$env:TEMP` ejecutando `pytest -q` con registro explícito de `sys.prefix` en `evidencias/pruebas/pytest_v0_venv.txt` (12 tests passed).
  4. Registro formal de no conformidad en `docs/gestion/nc01.md`.
- **Responsable:** E1 Borda Espinoza, Gabriela.
- **Estado:** Abierta (acciones correctivas ejecutadas; pendiente de verificación formal de cierre por E4).

---

## Corte 2

*pendiente: se registrara tras CR01 y revisiones*
