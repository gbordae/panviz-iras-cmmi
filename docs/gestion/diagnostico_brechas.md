# Diagnóstico Inicial de Brechas de Proceso — Piloto CMMI DEV v1.3 Panviz IRAS

| Metadato  | Valor                                              |
|-----------|----------------------------------------------------|
| Fecha     | 2026-11-08                                         |
| Autor     | E1 Borda Espinoza, Gabriela (Coordinación y mejora)|
| Estado    | cerrado para el corte 1                            |

> **Aclaración metodológica:** Las brechas descritas en este documento se refieren estrictamente a la **práctica de ingeniería y gestión del equipo de trabajo**. En ningún caso se atribuyen al sistema Panviz fallas, defectos o problemas operativos reales que no hayan sido formalmente observados o probados.
> Los riesgos e interesados asociados a este diagnóstico se encuentran detallados en docs/gestion/riesgos.csv.

---

## 1. Brechas identificadas contra el estado inicial (Commit 7c20069)

En el commit inicial (7c20069), el repositorio contaba únicamente con una estructura básica de directorios vacíos con archivos .gitkeep, un archivo .gitignore, 
equirements.txt básico y documentos de gestión en blanco (	ablero_tareas.csv, 
egistro_cambios.csv, indice_evidencias.csv). A partir de dicho estado inicial se identifican tres brechas principales:

### Brecha 1: Ausencia de Trazabilidad Bidireccional de Ingeniería

- **Evidencia inicial (7c20069):** Ausencia total de matriz o registro de trazabilidad; la carpeta docs/requisitos/ solo contenía un .gitkeep y no existía docs/gestion/trazabilidad.csv.
- **Consecuencia potencial:** Imposibilidad de vincular los requisitos con decisiones de diseño, módulos de código fuente y casos de prueba; riesgo de construir funcionalidad no solicitada o de liberar requisitos sin verificación formal.
- **Acción acordada:** Crear y mantener una matriz de trazabilidad bidireccional continua (docs/gestion/trazabilidad.csv) que relacione cada identificador de requisito (R01–R05, CR01) con su diseño, código, prueba, versión y estado.
- **Artefacto que la atiende:** docs/gestion/trazabilidad.csv, complementado con docs/requisitos/requisitos.md y docs/requisitos/diseno.md.
- **Estado actual según el repositorio:** Parcialmente atendida (R01–R04 trazados con diseño, código y pruebas en estado erificado por pruebas - pendiente de revision de codigo; R05 y CR01 pendientes).

---

### Brecha 2: Inexistencia de un Proceso Común y Criterios Estandarizados de Adaptación

- **Evidencia inicial (7c20069):** La carpeta docs/proceso/ contenía únicamente .gitkeep. No existían políticas de ciclo de vida, responsabilidades de rol, reglas de cambio ni criterios de adaptación para módulos CSV o formularios.
- **Consecuencia potencial:** Trabajo desarticulado entre integrantes, criterios dispersos sobre validación de datos, manipulación no controlada de cambios y sobrecarga documental si se intentaban usar herramientas pesadas.
- **Acción acordada:** Definir un Proceso Estándar v1.0 basado en un ciclo de 7 etapas con revisiones cruzadas (E1-E5), acompañado de una regla de adaptación (Caso A importación CSV vs Caso B formularios) y un juego de plantillas compactas en Markdown para reducir la carga documental.
- **Artefacto que la atiende:** docs/proceso/proceso_estandar_v1.md, docs/proceso/regla_adaptacion.md y plantillas en docs/proceso/plantillas/.
- **Estado actual según el repositorio:** Atendida a nivel documental en el repositorio (definido v1.0, pendiente de actualización a v2.0 tras lecciones de NC-01).

---

### Brecha 3: Carencia de Mecanismos Formales y Registros de Revisión por Pares

- **Evidencia inicial (7c20069):** Ausencia de listas de chequeo, actas de revisión o plantillas de aseguramiento de calidad; no existían pautas para revisar requisitos, código ni pruebas.
- **Consecuencia potencial:** Los defectos de codificación, violaciones de estándares o discrepancias con el diseño se propagan hacia fases avanzadas sin ser detectados tempranamente, dependiendo exclusivamente de la verificación individual del autor.
- **Acción acordada:** Institucionalizar la revisión por pares cruzada obligatoria mediante listas de chequeo explícitas (plantilla_revision.md), definiendo qué rol revisa a quién (E1 revisa E5, E2 revisa E3, E3 revisa E2, E4 revisa E3 auditado por E1) y preparando checklists técnicos antes de la liberación de cada línea base.
- **Artefacto que la atiende:** docs/proceso/plantillas/plantilla_revision.md y docs/gestion/revision_codigo_B1.md.
- **Estado actual según el repositorio:** En preparación (checklist técnico de B1 estructurado con casillas abiertas, pendiente de ejecución formal por parte del revisor E4).

---

## 2. Interesados y Gestión de Riesgos

La mitigación de estas brechas se encuentra vinculada a los riesgos del proyecto gestionados en docs/gestion/riesgos.csv:
- **R-01 (Cronograma y disponibilidad para revisiones):** Atiende la Brecha 3 mediante listas de chequeo breves y sesiones focalizadas de máximo 30 minutos (dueño: E1).
- **R-02 (Sesgo del oráculo y datos sintéticos):** Atiende la Brecha 1 asegurando que los oráculos se definan con anticipación y supuestos documentados antes de la codificación (dueño: E2).
- **R-03 (Cambio de reglas sin regresión):** Atiende la Brecha 2 mediante el flujo formal de 5 pasos para solicitudes de cambio (CR01) y regresión automatizada en pytest (dueño: E4).
