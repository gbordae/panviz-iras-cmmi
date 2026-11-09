# Plantilla de Caso de Prueba

| Campo                   | Valor |
|-------------------------|-------|
| **ID prueba**           | P01   |
| **Requisito asociado**  | R01   |
| **Entrada**             | CSV con 20 filas (15 válidas, 5 inválidas). |
| **Resultado esperado**  | 15 aceptadas, 5 rechazadas con motivo. |
| **Resultado observado** | 15 aceptadas, 5 rechazadas con motivo. |
| **Estado**              | Aprobado |
| **Fecha ejecución**     | 2026-11-09 |

## Notas
Oráculo en `datos/oraculo_rechazos.csv`. Comando: `pytest -q tests/test_importacion.py`.

---

| Campo                   | Valor |
|-------------------------|-------|
| **ID prueba**           | P02   |
| **Requisito asociado**  | R02   |
| **Entrada**             | Fila con campo obligatorio vacío (id). |
| **Resultado esperado**  | Rechazo con motivo "campo obligatorio vacío". |
| **Resultado observado** | Rechazo con motivo "campo obligatorio vacío". |
| **Estado**              | Aprobado |
| **Fecha ejecución**     | 2026-11-09 |

---

| Campo                   | Valor |
|-------------------------|-------|
| **ID prueba**           | P03   |
| **Requisito asociado**  | R02   |
| **Entrada**             | Fila con fecha imposible (2026-02-30). |
| **Resultado esperado**  | Rechazo con motivo "fecha imposible". |
| **Resultado observado** | Rechazo con motivo "fecha imposible". |
| **Estado**              | Aprobado |
| **Fecha ejecución**     | 2026-11-09 |

---

| Campo                   | Valor |
|-------------------------|-------|
| **ID prueba**           | P04   |
| **Requisito asociado**  | R02   |
| **Entrada**             | Fila duplicada (id repetido). |
| **Resultado esperado**  | Rechazo con motivo "clave duplicada". |
| **Resultado observado** | Rechazo con motivo "clave duplicada". |
| **Estado**              | Aprobado |
| **Fecha ejecución**     | 2026-11-09 |

---

| Campo                   | Valor |
|-------------------------|-------|
| **ID prueba**           | P05   |
| **Requisito asociado**  | R03   |
| **Entrada**             | 15 filas válidas conocidas. |
| **Resultado esperado**  | Consolidado por semana ISO, establecimiento, distrito y grupo etario correcto. |
| **Resultado observado** | Consolidado correcto. |
| **Estado**              | Aprobado |
| **Fecha ejecución**     | 2026-11-09 |

---

| Campo                   | Valor |
|-------------------------|-------|
| **ID prueba**           | P06   |
| **Requisito asociado**  | R04   |
| **Entrada**             | Exportación del consolidado. |
| **Resultado esperado**  | Reconciliación = 0 (suma consolidado – filas aceptadas). |
| **Resultado observado** | Reconciliación = 0. |
| **Estado**              | Aprobado |
| **Fecha ejecución**     | 2026-11-09 |


# Plantilla de Caso de Prueba (v2.0)

| Campo                       | Valor |
|-----------------------------|-------|
| **ID prueba**               | P07   |
| **Requisito asociado**      | CR01-R03 |
| **Entrada**                 | Consolidado con filtro por distrito "Lima". |
| **Resultado esperado**      | Solo filas del distrito Lima; reconciliación = 0 con filas válidas de Lima. |
| **Resultado observado**     | Solo filas de Lima; reconciliación = 0. |
| **Intérprete / sys.prefix** | `.venv` (Python 3.11) |
| **Versión de dependencias** | `requirements.txt` (pytest 8.x) |
| **Estado**                  | Aprobado |
| **Fecha ejecución**         | 2026-11-09 |

## Notas de trazabilidad y entorno
Comando: `pytest -q tests/test_cr01.py`. Suite de regresión P01–P06 ejecutada sin fallos. Evidencia en `evidencias/pruebas/P07.txt`.