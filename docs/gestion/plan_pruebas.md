# Plan de Pruebas y Resultados de Verificación — Panviz IRAS

| Metadato  | Valor                                              |
|-----------|----------------------------------------------------|
| Versión   | 1.0                                                |
| Fecha     | 2026-11-08                                         |
| Autor     | E4 Suclle Suca, Michael (Calidad y pruebas)        |
| Estado    | verificado por pruebas                             |

> **Nota sobre CR01:** Cuando se tramite la solicitud de cambio CR01 (filtro por distrito),
> se incorporará el caso de prueba **PR-07** y se ejecutará la suite completa de regresión
> (re-ejecución obligatoria de PR-01 a PR-06).

---

## Casos de Prueba (PR-01 a PR-06)

### PR-01 — Importación de datos y verificación de contrato de columnas

| Campo                   | Valor |
|-------------------------|-------|
| **ID prueba**           | PR-01 |
| **Requisito asociado**  | R01 |
| **Entrada**             | `datos/notificaciones_iras_sinteticas.csv` (20 filas válidas en estructura); archivos con columnas alteradas o incompletas en directorio temporal |
| **Resultado esperado**  | CSV sintético lee 20 filas en memoria; CSV con encabezado alterado o incompleto termina con código de salida 2 sin procesar filas |
| **Resultado observado** | 20 filas leídas correctamente; excepciones `SystemExit` capturadas con código 2 ante encabezados inválidos (`test_importacion.py` 3/3 passed) |
| **Estado**              | Aprobado |
| **Fecha ejecución**     | 2026-11-08 |

---

### PR-02 — Validación de campos obligatorios, evento y catálogo etario

| Campo                   | Valor |
|-------------------------|-------|
| **ID prueba**           | PR-02 |
| **Requisito asociado**  | R02 |
| **Entrada**             | Registros unitarios con campo `establecimiento` vacío, campo `evento` != `IRAS` (`COVID`), y `grupo_etario` no perteneciente al catálogo (`90+`) |
| **Resultado esperado**  | Rechazos exactos con motivos: `"campo obligatorio vacio (establecimiento)"`, `"evento distinto de IRAS"`, `"grupo etario fuera de catalogo"` |
| **Resultado observado** | Registros rechazados en fila_datos correspondiente con los literales exactos especificados (`test_validacion.py` 3/5 passed) |
| **Estado**              | Aprobado |
| **Fecha ejecución**     | 2026-11-08 |

---

### PR-03 — Validación de fechas imposibles o formato no estándar

| Campo                   | Valor |
|-------------------------|-------|
| **ID prueba**           | PR-03 |
| **Requisito asociado**  | R02 |
| **Entrada**             | Registros con fecha `2026-02-30` (calendario imposible) y `30/10/2026` (formato no ISO) |
| **Resultado esperado**  | Ambas filas rechazadas con motivo exacto `"fecha imposible"` |
| **Resultado observado** | Ambas filas capturadas y rechazadas con motivo `"fecha imposible"` (`test_validacion.py` 1/5 passed) |
| **Estado**              | Aprobado |
| **Fecha ejecución**     | 2026-11-08 |

---

### PR-04 — Validación de unicidad de clave y política de duplicados

| Campo                   | Valor |
|-------------------------|-------|
| **ID prueba**           | PR-04 |
| **Requisito asociado**  | R02 |
| **Entrada**             | Dos registros con el mismo identificador (`id = N007`) en filas consecutivas |
| **Resultado esperado**  | Se acepta la primera aparición; la segunda se rechaza con motivo exacto `"clave duplicada"` |
| **Resultado observado** | Primera fila aceptada como válida; segunda fila rechazada con motivo `"clave duplicada"` (`test_validacion.py` 1/5 passed) |
| **Estado**              | Aprobado |
| **Fecha ejecución**     | 2026-11-08 |

---

### PR-05 — Consolidación conocida y cálculo de semana ISO

| Campo                   | Valor |
|-------------------------|-------|
| **ID prueba**           | PR-05 |
| **Requisito asociado**  | R03 |
| **Entrada**             | Filas válidas del CSV sintético (15 registros); fechas límite de fin de año (`2026-12-31`, `2027-01-01`) |
| **Resultado esperado**  | Consolidado con exactamente 12 filas, suma de 15 casos, orden y valores idénticos a `datos/oraculo_consolidado.csv`; semanas ISO calculadas conforme a año ISO |
| **Resultado observado** | Coincidencia exacta fila por fila contra el oráculo cargado dinámicamente; cálculo de semana ISO verificado con `datetime.date.isocalendar()` (`test_consolidacion.py` 2/2 passed) |
| **Estado**              | Aprobado |
| **Fecha ejecución**     | 2026-11-08 |

---

### PR-06 — Reconciliación, formato de archivos y reporte de rechazos

| Campo                   | Valor |
|-------------------------|-------|
| **ID prueba**           | PR-06 |
| **Requisito asociado**  | R04 |
| **Entrada**             | Salida generada en directorio temporal a partir de las 20 filas sintéticas; caso simulado con descuadre en consolidación |
| **Resultado esperado**  | Retorno 0 en caso normal; archivos `consolidado.csv`, `rechazos.csv`, `resumen.txt` generados con encabezados exactos; `rechazos.csv` idéntico a `datos/oraculo_rechazos.csv`; `resumen.txt` con `diferencia_reconciliacion: 0`; retorno 3 ante descuadre |
| **Resultado observado** | Todos los encabezados validados; rechazos idénticos al oráculo; resumen con balance perfecto (20 leídas, 15 aceptadas, 5 rechazadas, 15 casos); código 3 retornado ante descuadre simulado (`test_reconciliacion_exportacion.py` 2/2 passed) |
| **Estado**              | Aprobado |
| **Fecha ejecución**     | 2026-11-08 |

---

## Resumen de Ejecución

- **Total de pruebas ejecutadas:** 12 tests en 4 archivos.
- **Pruebas aprobadas:** 12
- **Pruebas fallidas:** 0
- **Evidencia asociada:** `evidencias/pruebas/pytest_v0.txt`
