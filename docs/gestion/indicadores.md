# Indicadores de Proceso — Piloto Panviz IRAS

| Metadato    | Valor                                              |
|-------------|----------------------------------------------------|
| Autor       | E5 Ccoscco Alvis, Italo (Configuración y medición) |
| Estado      | consolidado (Corte 1 y Corte 2)                    |

> **Nota metodológica obligatoria:** *Umbrales propuestos por el docente; no prueban efectividad clínica, capacidad estadística de nivel 4 ni madurez organizacional.*
> Los presentes indicadores tienen fines exclusivos de seguimiento y aprendizaje del equipo durante el piloto académico CMMI DEV v1.3.

---

## Tabla de Indicadores — Corte 2 (2026-11-08)

| Indicador | Fórmula | Numerador | Denominador | Valor | Observación |
|:----------|:--------|:---------:|:-----------:|:-----:|:------------|
| **Trazabilidad de requisitos** | $\frac{\text{requisitos trazados}}{\text{alcance total (R01-R05 + CR01)}}$ | 5 | 6 | **83.33%** | sin línea base (5 de 6 con diseño, código y prueba: R01-R04 + CR01; R05 pendiente) |
| **Pruebas satisfactorias** | $\frac{\text{pruebas unitarias aprobadas}}{\text{pruebas ejecutadas}}$ | 19 | 19 | **100.00%** | sin línea base (19 funciones pytest pasaron; cubre los 7 IDs: PR-01 a PR-07) |
| **Detección de errores de datos** | $\frac{\text{filas inválidas detectadas}}{\text{esperadas según oráculo (5)}}$ | 5 | 5 | **100.00%** | sin línea base (5 de 5 rechazos esperados detectados con motivo exacto) |
| **Reconciliación de casos** | $\text{suma consolidado} - \text{aceptadas/distrito}$ | sin=15, cer=6, cay=5, yan=4 | sin=15, cer=6, cay=5, yan=4 | **0** | sin línea base (balance exacto: diferencia=0 en sin_filtro y en los 3 distritos: Cercado 0, Cayma 0, Yanahuara 0) |
| **Eficacia de formación** | $\frac{\text{integrantes con comprobación realizada}}{\text{total 5 integrantes}}$ | 0 | 5 | **0.00%** | sin línea base (sesión no ejecutada aún; casillas pendientes) |
| **Cumplimiento de revisiones por pares** | $\frac{\text{productos con revisión cerrada}}{\text{productos en registro_revisiones (5)}}$ | 1 | 5 | **20.00%** | sin línea base (1 de 5 cerradas: requisitos cerrada; código parcial; diseño, pruebas y liberación pendientes) |

---

## Comparación Corte 1 vs Corte 2

| Indicador | Corte 1 (2026-11-08 16:34) | Corte 2 (2026-11-08 19:22) | Estado de evolución observable |
|:----------|:--------------------------:|:--------------------------:|:-------------------------------|
| **Trazabilidad de requisitos** | 4/6 (66.67%) | 5/6 (83.33%) | Se incorporó CR01 con diseño (`diseno.md`), código (`filtro.py, cli.py`) y prueba (`PR-07`) |
| **Pruebas unitarias y regresión** | 12/12 (100.00%) | 19/19 (100.00%) | Se ejecutaron y aprobaron 7 pruebas nuevas para PR-07 manteniendo 100% de regresión en PR-01..PR-06 |
| **Detección de errores de datos** | 5/5 (100.00%) | 5/5 (100.00%) | Se mantiene la detección exacta del oráculo de rechazos sin alteraciones |
| **Reconciliación de casos** | 0 (discrepancia 0) | 0 (discrepancia 0) | Cuadre matemático verificado tanto a nivel global como individualizado por cada distrito |
| **Eficacia de formación** | 0/5 (0.00%) | 0/5 (0.00%) | Sesión de 15 min documentada en `guia_formacion_15min.md` aún pendiente de impartición |
| **Cumplimiento de revisiones por pares** | 0/3 (0.00%) | 1/5 (20.00%) | Formalizada revisión de requisitos (cerrada con Evidencia_03); código en estado parcial por cambios de CR01 |
