# Catálogo de Datos — Panviz IRAS

> **Nota:** Todos los datos son **sintéticos**, generados exclusivamente para el piloto CMMI DEV v1.3.
> Las reglas descritas aquí son **reglas de calidad de datos**, no criterios de diagnóstico clínico.

## Campos del registro de notificación

| Campo               | Tipo    | Obligatorio | Reglas de validación                                                                 |
|---------------------|---------|-------------|--------------------------------------------------------------------------------------|
| `id`                | Texto   | Sí          | Clave única por carga; un segundo registro con el mismo `id` es rechazado.           |
| `fecha_notificacion`| Fecha   | Sí          | Formato `YYYY-MM-DD`; debe ser una fecha calendario existente (sin días imposibles). |
| `establecimiento`   | Texto   | Sí          | No puede estar vacío ni ser solo espacios.                                           |
| `distrito`          | Texto   | Sí          | No puede estar vacío ni ser solo espacios.                                           |
| `grupo_etario`      | Texto   | Sí          | Debe pertenecer al catálogo etario (ver abajo).                                      |
| `evento`            | Texto   | Sí          | Debe ser exactamente `IRAS` para el piloto actual (ver abajo).                       |

## Catálogo etario (supuesto documentado del equipo)

Valores válidos exactos para el campo `grupo_etario`:

| Valor  | Descripción             |
|--------|-------------------------|
| `0-4`  | Niños de 0 a 4 años     |
| `5-14` | Niños/adolescentes 5-14 |
| `15-59`| Adultos 15 a 59 años    |
| `60+`  | Adultos mayores ≥ 60    |

> **Supuesto documentado:** El catálogo fue acordado por el equipo para el piloto.
> Cualquier valor fuera de este conjunto (p. ej. `90+`) debe ser rechazado con motivo
> `grupo etario fuera de catalogo`. Este supuesto deberá revisarse si el sistema se extiende.

## Catálogo de eventos (alcance del piloto)

| Valor  | Descripción                        |
|--------|------------------------------------|
| `IRAS` | Infección Respiratoria Aguda Severa|

> Para el piloto, solo se acepta el evento `IRAS`. Un registro con otro valor
> (p. ej. `COVID`) es rechazado con motivo `evento distinto de IRAS`.

## Clave de unicidad

La unicidad de los registros se determina por el campo **`id`**.
Si dos filas tienen el mismo `id`, la segunda fila es rechazada con motivo `clave duplicada`.

## Convención de reporte de rechazos

Los reportes de rechazo usan la columna **`fila_datos`**, que numera las filas de datos
comenzando en **1** (sin contar la fila de encabezado del CSV).

## Motivos de rechazo reconocidos

| Motivo                              | Descripción                                              |
|-------------------------------------|----------------------------------------------------------|
| `clave duplicada`                   | El `id` ya aparece en una fila anterior de la misma carga|
| `campo obligatorio vacio (campo)`   | Un campo obligatorio está vacío o ausente                |
| `fecha imposible`                   | La fecha no existe en el calendario gregoriano           |
| `evento distinto de IRAS`           | El campo `evento` no es `IRAS`                           |
| `grupo etario fuera de catalogo`    | El campo `grupo_etario` no está en el catálogo           |

