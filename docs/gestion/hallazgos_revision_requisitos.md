# Registro de Hallazgos de Revisión Técnica de Requisitos — Panviz IRAS

| Metadato         | Valor                                                    |
|------------------|----------------------------------------------------------|
| Fecha de reporte | 2026-11-08                                               |
| Hora de reporte  | [completar con la hora de la captura]                    |
| Reportado por    | E3 Fernandez Huarca, Rodrigo (Diseño y desarrollo)       |
| Medio de reporte | Chat grupal del equipo                                   |
| Revisor          |                                                          |
| Fecha de cierre  |                                                          |

---

## 1. Hallazgos Reportados por E3

### H-01: Indefinición del Comportamiento ante Fallo de Reconciliación en R04

- **Descripción:** El requisito R04 en docs/requisitos/requisitos.md especifica que se debe reconciliar el total del consolidado con los registros aceptados, pero no define el comportamiento del sistema ni el código de salida en caso de que ocurra una discrepancia (mientras que docs/requisitos/diseno.md y src/panviz/exportador.py sí establecen la terminación con código de salida 3).
- **Impacto:** Ambigüedad en el criterio de aceptación de R04 que genera una discrepancia documental entre los requisitos y el diseño técnico.
- **Estado:** aceptado - accion en curso
- **Acción acordada:** Actualizar docs/requisitos/requisitos.md elevando la versión a 0.2 para incluir explícitamente en el criterio de aceptación de R04 que, ante fallo de reconciliación, el programa termina con código de salida 3 y mensaje de error en stderr.
- **Evidencia:** captura pendiente de archivar en evidencias/revisiones/

---

### H-02: Indefinición del Tratamiento de Mayúsculas y Espacios en Filtro por Distrito (CR01)

- **Descripción:** En la propuesta inicial de CR01, la comparación del nombre de distrito se concibió como coincidencia de texto literal exacto; falta formalizar cómo debe responder el sistema si el usuario ingresa valores con variaciones de mayúsculas/minúsculas (p. ej. cercado, CERCADO) o espacios en los extremos.
- **Impacto:** Riesgo de inconsistencias en la experiencia de uso del CLI y de rechazos o filtros vacíos indeseados por diferencias de formato tipográfico.
- **Estado:** aceptado - accion en curso
- **Acción acordada:** Incorporar en la versión 0.2 de docs/gestion/CR01.md una regla de normalización (ignorar mayúsculas/minúsculas y recortar espacios en los extremos al evaluar el parámetro --distrito, manteniendo intactos los datos originales del archivo).
- **Evidencia:** captura pendiente de archivar en evidencias/revisiones/

---

## 2. Aportes de E2 al Criterio de Aceptación de CR01

Durante la revisión y refinamiento de la solicitud de cambio CR01, la integrante **E2 Meza Vizcarra, Cielo** (Requisitos y usuario simulado) aportó las siguientes precisiones esenciales:

1. **Verificación granular por semana y grupo etario:** No limitar la verificación del filtro a los totales agregados por distrito (6, 5 y 4 casos), sino exigir que el consolidado filtrado coincida fila por fila con las semanas ISO y grupos etarios correspondientes del oráculo (p. ej. en Cercado: W43 grupo 60+ = 2 casos; W44 grupo 5-14 = 1 caso y grupo 60+ = 1 caso; W45 grupo 60+ = 1 caso y grupo 5-14 = 1 caso; total = 6 casos distribuidos en 2 por semana).
2. **Invariabilidad de rechazos:** El archivo 
echazos.csv no debe verse afectado en absoluto por la opción de filtro (deben preservarse exactamente los 5 registros rechazados originales).
3. **Estructura extendida de 
esumen.txt y reconciliación contextual:** 
esumen.txt debe conservar las métricas globales (leidas: 20, ceptadas: 15, 
echazadas: 5) y añadir dos campos de trazabilidad: distrito_filtrado: <nombre> y ceptadas_del_distrito: <n>. La reconciliación bajo filtro debe comparar la suma del consolidado contra ceptadas_del_distrito.
