# Acta de Validación — Baseline B2 (Panviz IRAS)

> **IMPORTANTE:** Esta acta documenta la validación funcional con usuario simulado en el contexto del piloto CMMI DEV v1.3. **La validación del usuario simulado no equivale a la aprobación de una autoridad sanitaria real ni a un aval clínico.** Los datos validados son sintéticos.

| Campo               | Valor |
|---------------------|-------|
| **Usuario simulado**| E2 Meza Vizcarra, Cielo |
| **Fecha**           | 2026-11-08 |
| **Hora de capturas**| 20:30-20:32 (segun fecha de los archivos) |
| **Hora del mensaje de E2** | 20:55 (Evidencia_08) |
| **Commit validado** | `c7989fb` |
| **Confirmación del acta por E2** | confirmada (Evidencia_11, 2026-11-09 14:07) |

## Escenarios de validación

| Escenario | Entrada / condición | Resultado esperado | Resultado observado | Decisión | Evidencia |
|:---:|---|---|---|:---:|---|
| **V-01**  | Sin filtro (`--entrada datos/notificaciones_iras_sinteticas.csv`) | 20 leídas, 15 aceptadas, 5 rechazadas (filas 8, 11, 14, 17, 19), suma 15, diferencia 0 | leidas=20, aceptadas=15, rechazadas=5, suma=15, diferencia=0; rechazos en filas 8, 11, 14, 17 y 19. Conforme. | conforme, segun reporte de E2 | `evidencias/validacion/PruebaUsuario_01.png` |
| **V-02**  | `--distrito Cercado` | `distrito_filtrado: Cercado`, `aceptadas_del_distrito: 6`, `suma_consolidado: 6`, `diferencia_reconciliacion: 0`, 5 rechazos base | suma=6, aceptadas_del_distrito=6, mismos 5 rechazos. Conforme. | conforme, segun reporte de E2 | `evidencias/validacion/PruebaUsuario_02.png` |
| **V-03**  | `--distrito " cayma "` | `distrito_filtrado: cayma`, `aceptadas_del_distrito: 5`, `suma_consolidado: 5`, `diferencia_reconciliacion: 0`, 5 rechazos base | suma=5. Conforme. | conforme, segun reporte de E2 | `evidencias/validacion/PruebaUsuario_03.png` |
| **V-04**  | `--distrito Yanahuara` | `distrito_filtrado: Yanahuara`, `aceptadas_del_distrito: 4`, `suma_consolidado: 4`, `diferencia_reconciliacion: 0`, 5 rechazos base | suma=4. Conforme. | conforme, segun reporte de E2 | `evidencias/validacion/PruebaUsuario_04.png` |

## Decisión global

| Campo               | Valor |
|---------------------|-------|
| **Decisión final**  | conforme, segun reporte de E2 |
| **Observaciones**   | Confirmacion del acta por E2: confirmada (Evidencia_11, 2026-11-09 14:07). La validacion del usuario simulado no equivale a la aprobacion de una autoridad sanitaria real. Resultados recibidos por mensaje de E2 a las 20:55 (Evidencia_08) para el commit validado c7989fb. Evidencia del mensaje: `evidencias/revisiones/Evidencia_08.png`. |
