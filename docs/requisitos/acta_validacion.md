# Plantilla de Acta de Validación

> **IMPORTANTE:** Esta acta documenta la validación funcional con usuario simulado en el contexto
> del piloto CMMI DEV v1.3. **NO equivale a aprobación de autoridad sanitaria ni a aval clínico.**
> Los datos validados son sintéticos.

| Campo               | Valor |
|---------------------|-------|
| **Usuario simulado**| Cielo Meza (E2) |
| **Fecha**           | 2026-11-09 |

## Escenarios de validación

| Escenario | Entrada / condición | Resultado esperado | Resultado observado | Decisión |
|-----------|--------------------|--------------------|---------------------|----------|
| Importación CSV | 20 filas (15 válidas, 5 inválidas) | 15 aceptadas, 5 rechazadas con reporte | 15 aceptadas, 5 rechazadas con reporte | Aceptado |
| Consolidado semanal | 15 filas válidas | Agrupación por semana ISO, establecimiento, distrito y grupo etario | Agrupación correcta | Aceptado |
| CR01 (filtro por distrito) | Consolidado filtrado por "Lima" | Solo filas de Lima; reconciliación = 0 | Solo filas de Lima; reconciliación = 0 | Aceptado |

## Decisión global

| Campo               | Valor |
|---------------------|-------|
| **Decisión final**  | Aceptado |
| **Observaciones**   | Sin observaciones. El flujo cumple con R01–R05 y CR01. |