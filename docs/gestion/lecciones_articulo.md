# Lecciones Aprendidas del Estudio de Liberato, Varajao y Martins (2015)

| Metadato  | Valor                                              |
|-----------|----------------------------------------------------|
| Fecha     | 2026-11-08                                         |
| Autor     | E1 Borda Espinoza, Gabriela (Coordinación y mejora)|
| Referencia| Liberato, Varajao & Martins (2015). CMMI-DEV implementation practices. |

---

## Lecciones Clave y Aplicación en el Piloto Panviz IRAS

### Lección 1: Definición colaborativa de procesos con participación de los usuarios y ejecutores

- **Lección parafraseada:** La definición de procesos no debe imponerse como un marco teórico aislado; resulta indispensable involucrar activamente a quienes desempeñan los roles operativos y representan a los usuarios finales desde las fases iniciales, logrando que las prácticas reflejen necesidades reales y disminuyan la resistencia al cambio.
- **Página de referencia:** [p. por verificar]
- **Decisión aplicada en este piloto:** Se asignó formalmente el rol de Usuario Simulado y Requisitos a E2 (Cielo Meza), quien define el catálogo de datos, los requisitos R01–R05 y los criterios de aceptación medibles, participando en revisiones cruzadas con E3 (desarrollo).
- **Ruta del artefacto:** docs/requisitos/catalogo_datos.md y docs/requisitos/requisitos.md.

---

### Lección 2: Experimentación y validación gradual mediante proyectos piloto antes del despliegue general

- **Lección parafraseada:** Adoptar CMMI de manera abrupta en toda la organización incrementa significativamente el riesgo de fracaso; es más efectivo implementar y ajustar las prácticas en un alcance acotado y controlado (un proyecto piloto) para calibrar el esfuerzo, identificar no conformidades y consolidar lecciones antes de escalar.
- **Página de referencia:** [p. por verificar]
- **Decisión aplicada en este piloto:** Se acotó el alcance estrictamente a un piloto de 7 fases sobre el componente de importación, validación y consolidación de IRAS con datos sintéticos (20 registros), evaluando la capacidad de adaptación antes de abordar módulos mayores o de producción hospitalaria.
- **Ruta del artefacto:** docs/proceso/proceso_estandar_v1.md y docs/proceso/regla_adaptacion.md.

---

### Lección 3: Mitigación de la sobrecarga documental mediante plantillas concisas y soportes estandarizados

- **Lección parafraseada:** Una de las principales barreras en la institucionalización de CMMI es la burocracia documental excesiva; simplificar la documentación mediante plantillas cortas, directas y estandarizadas (de una sola página) integradas a los repositorios de trabajo habituales maximiza el valor agregado y el apego real del equipo al proceso.
- **Página de referencia:** [p. por verificar]
- **Decisión aplicada en este piloto:** Se diseñaron 7 plantillas compactas en Markdown dentro del propio repositorio Git (docs/proceso/plantillas/), prescindiendo de plataformas complejas o pesadas y manteniendo la trazabilidad directamente en archivos CSV livianos y versionados.
- **Ruta del artefacto:** docs/proceso/plantillas/ y docs/proceso/regla_adaptacion.md (sección reducción de carga documental).

---

## Nota de Limitaciones Metodológicas

> **Limitaciones del estudio:** La investigación de Liberato, Varajao y Martins (2015) recopila percepciones y opiniones cualitativas de un grupo específico de 22 jefes de proyecto durante una etapa temprana de adopción en un contexto organizacional particular. Por consiguiente, sus conclusiones reflejan tendencias orientativas y no garantizan que la réplica de estas decisiones en el presente proyecto académico genere automáticamente los mismos resultados de productividad o éxito.
