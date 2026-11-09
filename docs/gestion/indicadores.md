# Indicadores de Proceso — Corte 1 (Piloto Panviz IRAS)

| Metadato    | Valor                                              |
|-------------|----------------------------------------------------|
| Fecha corte | 2026-11-08                                         |
| Autor       | E5 Ccoscco Alvis, Italo (Configuración y medición) |
| Estado      | consolidado para Corte 1                           |

> **Nota metodológica obligatoria:** *Umbrales propuestos por el docente; no prueban efectividad clínica, capacidad estadística de nivel 4 ni madurez organizacional.*
> Los presentes indicadores tienen fines exclusivos de seguimiento y aprendizaje del equipo durante el piloto académico CMMI DEV v1.3.

---

## Tabla de Indicadores — Corte 1

| Indicador | Fórmula | Numerador | Denominador | Valor | Observación |
|:----------|:--------|:---------:|:-----------:|:-----:|:------------|
| **Trazabilidad de requisitos** | $\frac{\text{requisitos trazados}}{\text{alcance total (R01-R05 + CR01)}}$ | 4 | 6 | **66.67%** | sin línea base (4 de 6 con diseño, código y prueba; R05 y CR01 pendientes) |
| **Pruebas satisfactorias** | $\frac{\text{pruebas unitarias aprobadas}}{\text{pruebas ejecutadas}}$ | 12 | 12 | **100.00%** | sin línea base (12 funciones pytest pasaron; cubre PR-01 a PR-06) |
| **Detección de errores de datos** | $\frac{\text{filas inválidas detectadas}}{\text{esperadas según oráculo (5)}}$ | 5 | 5 | **100.00%** | sin línea base (5 de 5 rechazos esperados detectados con motivo exacto) |
| **Reconciliación de casos** | $\text{suma consolidado} - \text{registros aceptados}$ | 15 | 15 | **0** | sin línea base (balance exacto: 15 casos consolidados - 15 filas aceptadas = 0) |
| **Eficacia de formación** | $\frac{\text{integrantes con comprobación realizada}}{\text{total 5 integrantes}}$ | 0 | 5 | **0.00%** | sin línea base (sesión no ejecutada aún; casillas pendientes) |
| **Cumplimiento de revisiones por pares** | $\frac{\text{productos con revisión cerrada}}{\text{productos sometidos a revisión (3)}}$ | 0 | 3 | **0.00%** | sin línea base (revisiones preparadas en borrador; revisores aún no ejecutaron firmas) |

---

## Lectura e Interpretación de Resultados

1. **Ingeniería del componente (Trazabilidad, Pruebas y Validación de Datos):**
   - El núcleo funcional (R01 a R04) se encuentra completamente construido y verificado con 12 tests automatizados pasando al 100%, logrando un 66.67% de trazabilidad global (el restante 33.33% corresponde a la trazabilidad transversal R05 y a la solicitud de cambio CR01).
   - La calidad de datos y la consistencia matemática se cumplen con precisión de oráculo: 100% de errores sintéticos identificados y discrepancia de reconciliación en cero.

2. **Gestión y Calidad de Proceso (Formación y Revisiones):**
   - Los indicadores de formación (0%) y cumplimiento de revisiones (0%) reflejan que el proyecto se encuentra en la transición entre la construcción y la verificación formal por pares. Las guías y listas de chequeo existen documentalmente, pero su ejecución y firma están pendientes para las siguientes fases del cronograma.
