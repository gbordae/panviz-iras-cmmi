# Diseño del componente — Panviz IRAS

| Metadato  | Valor                                                                 |
|-----------|-----------------------------------------------------------------------|
| Versión   | 0.1                                                                   |
| Fecha     | 2026-11-08                                                            |
| Autor     | E3 Fernandez Huarca, Rodrigo                                          |
| Estado    | borrador — pendiente de revisión por E2 (requisitos) y E4 (calidad)  |

---

## Flujo general

```
CSV entrada
    │
    ▼
importar()   ← verifica contrato de encabezado (SystemExit 2 si falla)
    │  lista[dict bruto]
    ▼
validar()    ← aplica reglas fila a fila en orden definido
    │  (registros_validos, rechazos)
    ▼
consolidar() ← agrupa por semana ISO, establecimiento, distrito, grupo etario
    │  tabla_consolidado
    ▼
exportar()   ← escribe consolidado.csv, rechazos.csv, resumen.txt
    │  código de salida (0 ó 3)
    ▼
reconciliar  ← verificado dentro de exportar(); SystemExit 3 si diferencia ≠ 0
```

---

## Módulos en `src/panviz/`

| Archivo          | Responsabilidad                                                      |
|------------------|----------------------------------------------------------------------|
| `__init__.py`    | Declara el paquete; expone `__version__`                            |
| `__main__.py`    | Punto de entrada para `python -m panviz`; llama a `cli.main()`     |
| `cli.py`         | Parseo de argumentos con `argparse`; orquesta el pipeline completo  |
| `importador.py`  | Lee el CSV y verifica el contrato de encabezado                     |
| `validador.py`   | Valida cada fila según las reglas del catálogo; separa válidas/rechazadas |
| `consolidador.py`| Agrupa registros válidos por semana ISO y atributos; cuenta casos   |
| `exportador.py`  | Escribe los tres archivos de salida y ejecuta la reconciliación     |

### Interfaces (firmas y tipos)

```python
# importador.py
def importar(ruta: Path) -> list[dict[str, str]]:
    """Lee CSV y verifica encabezado. SystemExit(2) si contrato falla."""

# validador.py
def validar(filas: list[dict[str, str]]) -> tuple[list[dict], list[dict]]:
    """
    Retorna (registros_validos, rechazos).
    registros_validos: dicts con campos parseados; fecha como datetime.date.
    rechazos: dicts con fila_datos (int), id (str), motivo (str).
    """

# consolidador.py
def consolidar(validas: list[dict]) -> list[dict]:
    """
    Agrupa por (semana_iso, establecimiento, distrito, grupo_etario).
    Retorna lista de dicts con semana_iso, establecimiento, distrito,
    grupo_etario, casos (int).
    """

# exportador.py
def exportar(
    consolidado: list[dict],
    rechazos: list[dict],
    ruta_salida: Path,
    total_leidas: int,
) -> int:
    """
    Escribe consolidado.csv, rechazos.csv, resumen.txt.
    Retorna 0 si reconciliación OK, 3 si diferencia ≠ 0.
    """

# cli.py
def main() -> None:
    """Punto de entrada CLI. Orquesta el pipeline completo."""
```

---

## Contrato de entrada (encabezado CSV)

El encabezado debe ser **exactamente** (mismo orden, mismo texto, sin espacios extra):

```
id,fecha_notificacion,establecimiento,distrito,grupo_etario,evento
```

Si el encabezado del CSV no coincide con este contrato, el programa termina
con **código de salida 2** y un mensaje de error en stdout, sin procesar ninguna fila.

---

## Reglas de validación — orden de evaluación por fila

Las reglas se evalúan en este orden. Al detectar la primera infracción, la fila
es rechazada con el motivo correspondiente y no se evalúan las reglas siguientes.

| Orden | Regla | Motivo exacto en rechazos.csv |
|-------|-------|-------------------------------|
| 1 | Algún campo obligatorio está vacío o ausente | `campo obligatorio vacio (<campo>)` |
| 2 | La fecha no existe en el calendario gregoriano o no tiene formato YYYY-MM-DD | `fecha imposible` |
| 3 | El evento no es exactamente `IRAS` | `evento distinto de IRAS` |
| 4 | El grupo etario no está en `{0-4, 5-14, 15-59, 60+}` | `grupo etario fuera de catalogo` |
| 5 | El `id` ya apareció en una fila anterior de la misma carga | `clave duplicada` |

**Política de duplicados:** se acepta la **primera** aparición del `id`; todas las
siguientes son rechazadas con motivo `clave duplicada`.

> Los campos obligatorios son todos: `id`, `fecha_notificacion`, `establecimiento`,
> `distrito`, `grupo_etario`, `evento`. La evaluación de vacío se hace antes de parsear.

---

## Semana ISO

```python
import datetime
iso = fecha.isocalendar()   # (año_iso, semana, dia_semana)
semana_iso = f"{iso[0]}-W{iso[1]:02d}"   # ejemplo: "2026-W43"
```

- Se usa el **año ISO** (`iso[0]`), no el año calendario, para evitar errores en semanas de fin/inicio de año.
- Formato: `AAAA-Wss` con dos dígitos para la semana (p. ej. `W03`, `W43`).

---

## Orden del consolidado

1. **Primero:** por `semana_iso` (orden lexicográfico ascendente; funciona porque el formato es sorteable).
2. **Dentro de cada semana:** por orden de **primera aparición** del grupo en el archivo de entrada.

---

## Archivos de salida

### `consolidado.csv`
```
semana_iso,establecimiento,distrito,grupo_etario,casos
```

### `rechazos.csv`
```
fila_datos,id,motivo
```
- `fila_datos`: número de fila de datos (1-based, **sin contar el encabezado**).

### `resumen.txt`
```
leidas: <n>
aceptadas: <n>
rechazadas: <n>
suma_consolidado: <n>
diferencia_reconciliacion: <n>
```

---

## Reconciliación

```
diferencia = suma(casos en consolidado) - filas_aceptadas
```

- Si `diferencia == 0`: salida normal (código 0).
- Si `diferencia ≠ 0`: mensaje de error en stderr y **código de salida 3**.

La reconciliación garantiza que no se pierden ni duplican registros en el pipeline.

---

## Uso

```powershell
# PowerShell — desde la raíz del proyecto
$env:PYTHONPATH = "src"
python -m panviz --entrada datos\notificaciones_iras_sinteticas.csv --salida evidencias\ejecucion_v0
```

```bash
# bash/sh equivalente
PYTHONPATH=src python -m panviz --entrada datos/notificaciones_iras_sinteticas.csv --salida evidencias/ejecucion_v0
```

---

## Extensibilidad prevista

El consolidador (`consolidar()`) está diseñado como **función pura** que recibe
únicamente la lista de registros válidos y retorna la tabla consolidada sin efectos
secundarios. Esto facilita la adición de un futuro filtro (p. ej. por distrito)
sin modificar el pipeline de validación ni el exportador.

> **CR01 no está tramitado.** No se implementa ningún filtro por distrito en esta versión.
> Cuando se tramite, se agregará como parámetro opcional o como etapa intermedia
> entre `consolidar()` y `exportar()`, sin romper la interfaz existente.
