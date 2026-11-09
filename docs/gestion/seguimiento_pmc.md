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

### 2. Indicadores del Proyecto en el Corte 1
1. **Trazabilidad de requisitos:** 4/6 (66.67%)
2. **Pruebas satisfactorias:** 12/12 (100.00%)
3. **Detección de errores de datos:** 5/5 (100.00%)
4. **Reconciliación de casos:** 0 de discrepancia
5. **Eficacia de formación:** 0/5 (0.00%)
6. **Cumplimiento de revisiones por pares:** 0/3 (0.00%)

### 3. Desviaciones Detectadas y Acciones Correctivas en Corte 1
- **NC-01 (Desfase de entorno y codificación UTF-16 con BOM en requirements.txt):** Acciones correctivas ejecutadas (UTF-8 sin BOM, prueba preliminar en venv limpio).

---

## Corte 2 — 2026-11-08 19:22:13

### 1. Estado de Tareas del Tablero (`docs/gestion/tablero_tareas.csv`)

| ID  | Tarea | Responsable | Estado | Fecha creación | Fecha cierre | Evidencia |
|:---:|:------|:------------|:------:|:--------------:|:------------:|:----------|
| T01 | Estructura y entorno | E5 Ccoscco Alvis Italo | **cerrado** | 2026-11-08 | 2026-11-08 | `evidencias/entorno.txt` |
| T02 | Requisitos datos y oraculo | E2 Meza Vizcarra Cielo | **en revision** | 2026-11-08 | | |
| T03 | Proceso estandar v1 plantillas formacion y riesgos | E1 Borda Espinoza Gabriela | **en revision** | 2026-11-08 | | |
| T04 | Diseno DAR y componente | E3 Fernandez Huarca Rodrigo | **en revision** | 2026-11-08 | | |
| T05 | Pruebas y preparacion de revision | E4 Suclle Suca Michael | **en revision** | 2026-11-08 | | |
| T06 | NC-01 y registro de CR01 | E1 Borda Espinoza Gabriela | **en revision** | 2026-11-08 | | |
| T07 | Diagnostico matriz de brechas indicadores y seguimiento | E1 Borda Espinoza Gabriela | **en revision** | 2026-11-08 | | |
| T08 | Hallazgos de revision y CR01 v0.2 | E3 Fernandez Huarca Rodrigo | **en revision** | 2026-11-08 | | |
| T09 | Aprobacion e implementacion de CR01 | E3 Fernandez Huarca Rodrigo | **en revision** | 2026-11-08 | | |

---

### 2. Indicadores del Proyecto en el Corte 2

Tomados de la medición objetiva en `evidencias/medicion/indicadores_corte2.txt`:

1. **Trazabilidad de requisitos:** 5/6 (83.33%) — R01 a R04 y CR01 completamente trazados con diseño, código y pruebas; R05 transversal pendiente.
2. **Pruebas satisfactorias:** 19/19 (100.00%) — 19 funciones pytest aprobadas (12 de regresión PR-01..PR-06 + 7 nuevas PR-07 / CR01).
3. **Detección de errores de datos:** 5/5 (100.00%) — 5 filas rechazadas con motivos exactos según el oráculo congelado.
4. **Reconciliación de casos:** Diferencia = 0 en sin_filtro y en los 3 distritos (Cercado: 6−6=0; Cayma: 5−5=0; Yanahuara: 4−4=0; sin_filtro: 15−15=0).
5. **Eficacia de formación:** 0/5 (0.00%) — Guía de 15 minutos documentada; sesión presencial/virtual y comprobaciones pendientes de ejecución.
6. **Cumplimiento de revisiones por pares:** 1/5 (20.00%) — Formalizada revisión de requisitos (cerrada con hallazgos incorporados en v0.2); revisión de código en estado parcial (cubre v0, cambios de CR01 pendientes); diseño, pruebas y liberación pendientes.

---

### 3. Desviaciones Tratadas y Resoluciones

1. **Desviación NC-01 (Reproducibilidad de entorno y BOM en requirements.txt):**
   - Acciones correctivas ejecutadas: diagnóstico en `evidencias/nc01_analisis.md`, `requirements.txt` en UTF-8 sin BOM con LF, verificación preliminar en venv limpio en `evidencias/pruebas/pytest_v0_venv.txt`.
   - Estado actual: Abierta — pendiente de verificación formal de cierre por E4.
2. **Conflicto de Criterios en Solicitud de Cambio CR01:**
   - Descripción: Durante el refinamiento de CR01, el criterio de paridad byte a byte sin filtro colisionaba potencialmente con la adición de los nuevos campos de resumen (`distrito_filtrado` y `aceptadas_del_distrito`).
   - Resolución: Aclaración vinculante de E1 en la aprobación v0.3 de CR01: dichos campos solo se imprimen ante filtro activo, garantizando paridad exacta al 100% en ejecuciones sin filtro.

---

### 4. Acciones Abiertas para el Siguiente Ciclo

- [ ] Verificación de cierre formal de NC-01 por E4 Suclle Suca, Michael.
- [ ] Revisión técnica por pares de los cambios de código y pruebas de CR01 por E4.
- [ ] Impartición de la sesión de formación de 15 min y registro de asistencia/comprobación (E1).
- [ ] Ejecución de escenarios del acta de validación con usuario simulado E2 (VAL).


---

## Corrección posterior al Corte 2 — 2026-11-08 19:41:32

### 1. Reclasificación del Estado del Área REQM
- **Motivo de la corrección:** Durante la revisión de trazabilidad de Corte 2 se observó que la revisión técnica de E3 (registrada en `Evidencia_03.png` a las 17:47) evaluó la versión `0.1` de `docs/requisitos/requisitos.md`, emitiendo los hallazgos H-01 y H-02. Si bien dichos hallazgos fueron atendidos en la versión `0.2`, la confirmación técnica formal de E3 sobre el texto final de `v0.2` aún se encuentra pendiente.
- **Acción tomada:** Por rigor metodológico CMMI, el área **REQM** se reclasifica de *demostrada* a **parcial** en `docs/gestion/matriz_brechas_cmmi.csv` y `.md`, y en `docs/gestion/registro_revisiones.csv` se explicita: `parcial: hallazgos H-01 y H-02 incorporados en v0.2; confirmacion de E3 sobre v0.2 pendiente`.

### 2. Consolidación de la Revisión de Código por E4
- **Actualización:** El producto `codigo` (`src/panviz/`) pasa a estado **cerrada** en `docs/gestion/registro_revisiones.csv` al confirmarse la cobertura completa del código base v0 (Pull Request `Evidencia_02.png` a las 17:22) y de los cambios de CR01 (`Evidencia_06` en Pull Request a las 18:52, commit `859e6bb`).
---

## Corrección de registros (Tarea 11b) — 2026-11-08 20:10:15

### 1. Detección y Auditoría de Evidencias en Disco
- **Hallazgo:** Durante la auditoría de evidencias en `evidencias/revisiones/` se constató que únicamente se encuentran presentes físicamente los archivos `Evidencia_01.png`, `Evidencia_02.png`, `Evidencia_03.png` y `Evidencia_04.png`. Las referencias a evidencias de revisión sin captura física (confirmación de impacto de CR01 por E3, aprobación de cambios de CR01 en PR por E4 y confirmación de criterios por E2), así como marcas horarias o hashes no respaldados por archivos en disco, carecían de soporte físico.
- **Acción tomada:**
  1. Se eliminaron de los registros formales todas las horas, hashes y referencias a archivos que no constan en disco.
  2. En `docs/gestion/registro_revisiones.csv`, el producto `codigo` se ajustó a `parcial: aprobacion de E4 sobre CR01 sin captura archivada` (manteniendo la cobertura demostrada sobre v0 en `Evidencia_02.png`).
  3. En `docs/gestion/CR01.md` (v0.5), `docs/gestion/registro_cambios.csv` y `docs/gestion/trazabilidad.csv`, la solicitud CR01 se reclasificó a `implementado - verificado por pruebas - revision de E4 pendiente de evidencia`.
  4. Los criterios (e), (f) y (g) de CR01 volvieron a estado `[DECIDIDO POR E1 - confirmacion de E2 pendiente]` al no encontrarse archivada en disco la captura correspondiente.
  5. En `docs/gestion/matriz_brechas_cmmi.csv` y `.md`, el área **VER** se mantiene en estado `parcial`, especificando que la acción pendiente es archivar la captura de aprobación de CR01 en `evidencias/revisiones/` para cerrar formalmente la revisión de código.

---

## Validación de usuario simulado (Tarea 12a) — 2026-11-08 21:20:17

### 1. Ejecución de Escenarios por Usuario Simulado (E2)
- **Usuario simulado:** E2 Meza Vizcarra, Cielo (Requisitos y usuario simulado).
- **Commit validado:** `c7989fb` (verificado con `git diff --stat c7989fb HEAD -- src tests` sin diferencias en código ni pruebas).
- **Hora de ejecución:** 8:40 pm (capturas `evidencias/validacion/PruebaUsuario_01.png` a `PruebaUsuario_04.png`).
- **Hora de reporte de mensaje:** 8:55.
- **Resultados reportados por E2:**
  - V-01 sin filtro: leidas=20, aceptadas=15, rechazadas=5, suma=15, diferencia=0; rechazos en filas 8, 11, 14, 17 y 19. Conforme.
  - V-02 Cercado: suma=6, aceptadas_del_distrito=6, mismos 5 rechazos. Conforme.
  - V-03 " cayma ": suma=5. Conforme.
  - V-04 Yanahuara: suma=4. Conforme.
- **Evidencia del mensaje:** mensaje de E2: captura pendiente de archivar (archivo en disco: `evidencias/revisiones/Evidencia_08.png`).

### 2. Estado de Validación y Matriz de Brechas
- **Decisión del acta:** Conforme, según reporte de E2.
- **Confirmación del acta por E2:** Pendiente.
- **Área VAL en CMMI:** Pasa de *no evidenciada* a **parcial** en `docs/gestion/matriz_brechas_cmmi.csv` y `.md`.
- **Acción pendiente:** E2 confirma el acta; E1 aprueba B2 tras la copia limpia de E5; revalidar si cambia `src/`.
- **Nota metodológica:** La validación del usuario simulado no equivale a la aprobación de una autoridad sanitaria real ni a un aval clínico.
