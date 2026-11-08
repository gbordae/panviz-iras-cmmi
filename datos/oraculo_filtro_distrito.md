# Oráculo — Filtro por Distrito (CR01)

> **Nota:** CR01 (filtro por distrito) **aún NO está solicitado ni implementado**.
> Este documento registra el resultado esperado para cuando se tramite formalmente la solicitud de cambio.

## Resultado esperado para CR01

Dado el conjunto de **15 registros válidos** (tras aplicar las reglas de rechazo del oráculo), el filtro por distrito debe devolver los siguientes totales:

| Distrito   | Casos esperados |
|------------|-----------------|
| Cercado    | 6               |
| Cayma      | 5               |
| Yanahuara  | 4               |
| **Total**  | **15**          |

## Derivación (trazabilidad con oráculo_consolidado.csv)

| Distrito   | Semanas y grupos                                         | Suma |
|------------|----------------------------------------------------------|------|
| Cercado    | W43: 60+(2) · W44: 5-14(1)+60+(1) · W45: 60+(1)+5-14(1)| 6    |
| Cayma      | W43: 0-4(1)+5-14(1) · W44: 0-4(2) · W45: 15-59(1)      | 5    |
| Yanahuara  | W43: 15-59(1) · W44: 15-59(2) · W45: 0-4(1)            | 4    |

## Restricción

Este oráculo es un **supuesto de diseño** documentado antes de la implementación.
No representa aprobación formal ni solicitud de cambio activa.
CR01 se agregará a `trazabilidad.csv` y `registro_cambios.csv` cuando se tramite formalmente.

