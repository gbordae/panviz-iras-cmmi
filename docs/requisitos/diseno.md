# Diseño del componente — Panviz IRAS

| Metadato  | Valor                                                                 |
|-----------|-----------------------------------------------------------------------|
| Versión   | 0.2                                                                   |
| Fecha     | 2026-11-08                                                            |
| Autor     | E3 Fernandez Huarca, Rodrigo                                          |
| Estado    | diseño actualizado con CR01 aprobado                                  |

---

## Flujo general

```
CSV entrada
    │
    ▼
importar()               ← verifica contrato de encabezado (SystemExit 2 si falla)
    │  lista[dict bruto]
    ▼
validar()                ← aplica reglas fila a fila en orden definido
    │  (registros_validos, rechazos)
    ▼
[filtrar_por_distrito()] ← etapa opcional CR01 si se indica --distrito
    │  registros_a_consolidar
    ▼
consolidar()             ← función pura: agrupa por semana ISO, establecimiento, distrito, grupo etario
    │  tabla_consolidado
    ▼
exportar()               ← escribe consolidado.csv, rechazos.csv, resumen.txt
    │  código de salida (0 ó 3)
    ▼
reconciliar              ← verificado dentro de exportar(); SystemExit 3 si diferencia ≠ 0
```

---

## Módulos en `src/panviz/`

| Archivo          | Responsabilidad                                                      |
|------------------|----------------------------------------------------------------------|
| `__init__.py`    | Declara el paquete; expone `__version__`                            |
| `__main__.py`    | Punto de entrada para `python -m panviz`; llama a `cli.main()`     |
| `cli.py`         | Parseo de argumentos con `argparse` (incluye `--distrito`); orquesta el pipeline completo |
| `importador.py`  | Lee el CSV y verifica el contrato de encabezado                     |
| `validador.py`   | Valida cada fila según las reglas del catálogo; separa válidas/rechazadas |
| `filtro.py`      | Nueva función de filtrado por distrito previa al consolidador (CR01)|
| `consolidador.py`| Agrupa registros válidos por semana ISO y atributos; cuenta casos   |
| `exportador.py`  | Escribe los tres archivos de salida y ejecuta la reconciliación     |

### Interfaces (firmas y tipos)

```python
# importador.py
def importar(ruta: Path) -> list[dict[str, str]]:
    """Lee CSV y verifica encabezado. SystemExit(2) si contrato falla."""

# validador.py
def validar(filas: list[dict[str, str]]) -> tuple[list[dict], list[dict]]:
    """Retorna (registros_validos, rechazos)."""

# filtro.py (CR01)
def filtrar_por_distrito(
    validas: list[dict],
    distrito: str | None
) -> tuple[list[dict], int]:
    """
    Filtra registros válidos por nombre de distrito.
    Normalización: strip() y casefold(). No modifica datos originales.
    Retorna (registros_filtrados, total_aceptadas_distrito).
    """

# consolidador.py (función pura)
def consolidar(validas: list[dict]) -> list[dict]:
    """Agrupa por (semana_iso, establecimiento, distrito, grupo_etario)."""

# exportador.py
def exportar(
    consolidado: list[dict],
    rechazos: list[dict],
    ruta_salida: Path,
    total_leidas: int,
    distrito_filtrado: str | None = None,
    aceptadas_del_distrito: int | None = None,
) -> int:
    """Escribe salidas y reconcilia. Retorna 0 si OK, 3 si descuadre."""
```

---

## Contrato de entrada (encabezado CSV)

El encabezado debe ser **exactamente** en este orden:
```
id,fecha_notificacion,establecimiento,distrito,grupo_etario,evento
```
Si el contrato falla, termina con **código de salida 2** sin procesar filas.

---

## Reglas de validación — orden de evaluación por fila

1. Campo obligatorio vacío (`"campo obligatorio vacio (<campo>)"`)
2. Fecha imposible o formato no YYYY-MM-DD (`"fecha imposible"`)
3. Evento distinto de IRAS (`"evento distinto de IRAS"`)
4. Grupo etario fuera del catálogo (`"grupo etario fuera de catalogo"`)
5. Clave duplicada (`"clave duplicada"`, política: acepta primera aparición, rechaza posteriores)

---

## Especificación técnica de CR01 (Filtro por distrito)

- **Parámetro CLI:** `--distrito <nombre>` (opcional).
- **Función de filtro:** Se aplica exclusivamente sobre la lista de registros aceptados provenientes de `validar()`. La función `consolidar()` se preserva intacta como función pura.
- **Normalización de texto:** Se comparan los nombres aplicando `strip().casefold()`, asegurando que entradas como `"cayma"`, `"Cayma"`, `" CAYMA "` coincidan sin alterar los datos textuales originales del archivo.
- **Invariabilidad de rechazos:** `rechazos.csv` es completamente independiente del filtro (mantiene las 5 filas rechazadas en la carga).
- **Ajuste en `resumen.txt`:**
  - Sin filtro: líneas tradicionales (`leidas: 20`, `aceptadas: 15`, `rechazadas: 5`, `suma_consolidado: 15`, `diferencia_reconciliacion: 0`).
  - Con filtro: añade `distrito_filtrado: <nombre>` y `aceptadas_del_distrito: <n>`.
- **Reconciliación contextual:**
  - Con filtro: `diferencia = suma_consolidado - aceptadas_del_distrito`. Si es distinta de 0, código de salida 3.
  - Sin filtro: `diferencia = suma_consolidado - total_aceptadas`.
- **Distrito sin registros aceptados:**
  - Produce un archivo `consolidado.csv` con encabezado exacto y 0 filas de datos.
  - `suma_consolidado: 0`, `aceptadas_del_distrito: 0`, `diferencia_reconciliacion: 0`.
  - Agrega línea de advertencia informativa en `resumen.txt`: `AVISO: el distrito '<nombre>' no presenta registros aceptados.`

---

## Historial de cambios

| Versión | Fecha | Descripción del cambio | Origen |
|:---:|:---:|:---|:---:|
| 0.1 | 2026-11-08 | Diseño inicial del componente Panviz IRAS | E3 Fernandez Huarca, Rodrigo |
| 0.2 | 2026-11-08 | Incorporación del filtro opcional por distrito (CR01 aprobado), normalización y resumen contextual | CR01 v0.3 / E1 |
