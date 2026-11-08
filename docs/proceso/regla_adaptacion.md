# Regla de Adaptación del Proceso Estándar — Panviz IRAS

> **Propósito:** Definir cómo el proceso estándar v1.0 se aplica (o se adapta) según el tipo de módulo,
> sin abandonar los principios de trazabilidad y verificación del piloto CMMI DEV v1.3.

---

## Tabla: qué se mantiene / qué se adapta / qué se omite

| Elemento del proceso estándar           | Caso A: Importación CSV        | Caso B: Entrada por formulario  |
|-----------------------------------------|--------------------------------|---------------------------------|
| Oráculo definido antes de codificar     | **Se mantiene**                | **Se mantiene**                 |
| Prueba de contrato de columnas          | **Se mantiene** (obligatorio)  | Se adapta → validación en origen|
| Validación fila a fila                  | **Se mantiene**                | Se adapta → campo a campo       |
| Reporte de rechazos con `fila_datos`    | **Se mantiene**                | Se adapta → ID de formulario    |
| Plantilla de revisión antes de etapa    | **Se mantiene**                | **Se mantiene**                 |
| Plantilla de acta de validación         | **Se mantiene**                | **Se mantiene**                 |
| Gestión de ramas para CR               | **Se mantiene**                | **Se mantiene**                 |
| Prueba de contrato HTTP / esquema JSON  | Se omite (no aplica)           | Se adapta → se agrega si hay API|
| Formulario de captura en UI             | Se omite (no aplica)           | **Se mantiene** (obligatorio)   |
| Validación de rangos en campo numérico  | Se adapta → grupo etario       | **Se mantiene**                 |

---

## Caso A — Importación CSV (este piloto)

**Descripción:** El módulo recibe un archivo CSV como entrada principal.

### Pasos de verificación específicos para Caso A

1. **Prueba de contrato de columnas:** verificar que el encabezado del CSV contiene exactamente
   los campos `id,fecha_notificacion,establecimiento,distrito,grupo_etario,evento` en ese orden.
   Si el contrato falla, el módulo rechaza el archivo completo antes de procesar filas.

2. **Validación fila a fila:** cada fila se evalúa contra las reglas del `catalogo_datos.md`:
   - Campo obligatorio vacío → rechazo con motivo `campo obligatorio vacio (campo)`.
   - Fecha inexistente en el calendario → rechazo con motivo `fecha imposible`.
   - `id` ya visto en la misma carga → rechazo con motivo `clave duplicada`.
   - `evento` ≠ `IRAS` → rechazo con motivo `evento distinto de IRAS`.
   - `grupo_etario` fuera del catálogo → rechazo con motivo `grupo etario fuera de catalogo`.

3. **Reporte de rechazos:** se emite un listado con `fila_datos` (1-based, sin encabezado) y `motivo_esperado`,
   reconciliable con `datos/oraculo_rechazos.csv`.

---

## Caso B — Entrada por formulario

**Descripción:** El módulo recibe datos ingresados manualmente a través de un formulario (UI o API).

### Adaptaciones para Caso B

1. **Validación en origen:** los campos obligatorios, tipos y rangos se validan en el formulario
   antes de enviar al backend (validación cliente).
2. **Validación de respaldo en backend:** el backend revalida todos los campos para garantizar
   integridad, incluso si el cliente falla.
3. **Identificación de rechazo:** en lugar de `fila_datos`, se usa el identificador del formulario
   o el campo `id` de sesión.
4. **Contrato de columnas:** no aplica para entrada de formulario; en su lugar se define un esquema
   de campos (nombre, tipo, obligatorio, rango) equivalente al catálogo de datos.

---

## Aplicación al piloto Panviz IRAS

El piloto actual corresponde íntegramente al **Caso A** (importación CSV).

| Decisión de adaptación                        | Justificación                                      |
|-----------------------------------------------|----------------------------------------------------|
| Contrato de columnas es obligatorio            | El CSV puede provenir de distintos sistemas; el orden exacto evita errores silenciosos |
| Reporte usa `fila_datos` (1-based)             | Convención documentada en `catalogo_datos.md`; facilita trazabilidad con el oráculo   |
| Sin validación de UI                           | No hay formulario en este piloto                   |
| CR01 (filtro por distrito) → Caso A            | Si se tramita, es una consulta post-carga; no cambia el mecanismo de importación      |

---

## Nota de reducción de carga documental

> En lugar de herramientas pesadas (DOORS, Jira, Confluence), el piloto usa **plantillas cortas
> en Markdown** (una página por plantilla) almacenadas en `docs/proceso/plantillas/`.
> Esto reduce la fricción de adopción y mantiene los documentos versionados en Git
> junto al código, facilitando la trazabilidad sin infraestructura adicional.
