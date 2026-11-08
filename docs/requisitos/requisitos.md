# Requisitos del Sistema — Panviz IRAS

| Metadato | Valor |
|---|---|
| Versión | 0.2 |
| Fecha | 2026-11-08 |
| Responsable de definición | E2 Meza Vizcarra, Cielo |

> **Estado general:** Todos los requisitos están en borrador — pendiente de revisión técnica (E3) y aprobación de línea base B0 (E1).
> No se registran aprobaciones ni firmas en este documento.

## Tabla de requisitos

| ID  | Descripción | Criterio de aceptación | Responsable de definición | Responsable de implementación | Estado |
|-----|-------------|------------------------|---------------------------|-------------------------------|--------|
| R01 | Importar registros CSV con los campos: `id`, `fecha_notificacion`, `establecimiento`, `distrito`, `grupo_etario`, `evento`. | El sistema carga las 20 filas del CSV sintético sin error de lectura; los 20 registros quedan accesibles en memoria para las siguientes etapas. | E2 Meza Vizcarra, Cielo | E3 Fernandez Huarca, Rodrigo | borrador — pendiente de revisión técnica (E3) y aprobación de línea base B0 (E1) |
| R02 | Rechazar registros que incumplan las reglas de calidad: campos obligatorios vacíos, fechas imposibles, claves duplicadas, evento distinto de `IRAS`, grupo etario fuera del catálogo `{0-4, 5-14, 15-59, 60+}`; emitir reporte con `fila_datos` y motivo. | El módulo rechaza exactamente las 5 filas del `oraculo_rechazos.csv` (filas 8, 11, 14, 17, 19) con los motivos exactos indicados; no rechaza ninguna de las 15 filas válidas. | E2 Meza Vizcarra, Cielo | E3 Fernandez Huarca, Rodrigo | borrador — pendiente de revisión técnica (E3) y aprobación de línea base B0 (E1) |
| R03 | Consolidar los registros válidos agrupando por semana ISO (`isocalendar`), establecimiento, distrito y grupo etario; contar casos por grupo. | El consolidado generado coincide celda a celda con `oraculo_consolidado.csv` (12 filas, 4 grupos de semana ISO, total 15 casos). | E2 Meza Vizcarra, Cielo | E3 Fernandez Huarca, Rodrigo | borrador — pendiente de revisión técnica (E3) y aprobación de línea base B0 (E1) |
| R04 | Exportar el consolidado a CSV y reconciliar su total de casos con el número de registros aceptados. | El CSV exportado tiene exactamente 12 filas de datos; la suma de la columna casos es 15; esta cifra coincide con el recuento de registros no rechazados (20 − 5 = 15); si la reconciliacion no es 0, el programa termina con codigo de salida 3 y un mensaje de error. | E2 Meza Vizcarra, Cielo | E3 Fernandez Huarca, Rodrigo | borrador — pendiente de revisión técnica (E3) y aprobación de línea base B0 (E1) |
| R05 | Mantener trazabilidad completa entre requisitos, decisiones de diseño, código fuente, casos de prueba y versión liberada mediante `trazabilidad.csv` y el historial de control de configuración. | Cada requisito R01–R05 tiene al menos una fila en `trazabilidad.csv`; cada cambio tiene entrada en `registro_cambios.csv`; toda evidencia nueva tiene entrada en `indice_evidencias.csv`; el commit de liberación está etiquetado. | E2 Meza Vizcarra, Cielo | E5 Ccoscco Alvis, Italo | borrador — pendiente de revisión técnica (E3) y aprobación de línea base B0 (E1) |


## Historial de cambios

| Versión | Fecha | Descripción del cambio | Origen |
|:---:|:---:|:---|:---:|
| 0.1 | 2026-11-08 | Versión inicial de requisitos R01 a R05 | Definición inicial (E2) |
| 0.2 | 2026-11-08 | R04 aclara codigo de salida 3 | origen H-01 |
