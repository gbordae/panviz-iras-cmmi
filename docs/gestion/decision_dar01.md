# DAR01 — Decisión de Librería de Lectura CSV

| Campo                        | Valor                                                              |
|------------------------------|--------------------------------------------------------------------|
| ID decisión                  | DAR01                                                              |
| Título                       | Librería de lectura y procesamiento CSV                            |
| Estado                       | DECIDIDA — Alternativa A aprobada por E1 Borda Espinoza Gabriela  |
| Participantes de la decisión | E1 Borda Espinoza Gabriela (decisor final)                         |
| Fecha de confirmación        | 2026-11-09 (fecha real de registro; decision comunicada por E1 el 2026-11-08 ~22:40 segun E1; sin registro previo en el repositorio; registrada el 2026-11-09 15:34:09) |
| Decisor final (E1)           | E1 Borda Espinoza Gabriela — Alternativa A (biblioteca estandar CSV stdlib) |

---

## Alternativas evaluadas

### Alternativa A — `csv` + `datetime` (biblioteca estándar de Python)

Usar exclusivamente los módulos `csv`, `datetime`, `argparse`, `pathlib` y `sys`
de la biblioteca estándar. Las reglas de validación se implementan como funciones
Python explícitas, con bucles y condicionales legibles.

### Alternativa B — `pandas`

Usar `pandas` para leer el CSV como `DataFrame` y aplicar operaciones vectorizadas
para validación, agrupación y conteo.

---

## Criterios de evaluación (pesos suman 100)

| Criterio                              | Peso |
|---------------------------------------|------|
| Instalación y dependencias            | 25   |
| Trazabilidad y claridad de las reglas | 25   |
| Reproducibilidad en copia limpia      | 25   |
| Esfuerzo de desarrollo                | 15   |
| Rendimiento con volúmenes mayores     | 10   |
| **Total**                             | **100** |

---

## Tabla de puntajes (escala 1 = peor, 5 = mejor)

| Criterio                              | Peso | A (stdlib) | A×peso | B (pandas) | B×peso |
|---------------------------------------|------|-----------|--------|-----------|--------|
| Instalación y dependencias            | 25   | 5         | 125    | 2         | 50     |
| Trazabilidad y claridad de las reglas | 25   | 5         | 125    | 3         | 75     |
| Reproducibilidad en copia limpia      | 25   | 5         | 125    | 2         | 50     |
| Esfuerzo de desarrollo                | 15   | 3         | 45     | 5         | 75     |
| Rendimiento con volúmenes mayores     | 10   | 2         | 20     | 5         | 50     |
| **Total ponderado**                   |      |           | **440**|           | **300**|

---

## Comparación honesta

### A — Biblioteca estándar

**Ventajas:**
- Cero dependencias externas: funciona en cualquier instalación Python 3.x sin `pip install`.
- Las reglas de validación se escriben como funciones Python explícitas (bucle fila a fila),
  lo que facilita auditar y trazar la lógica contra el catálogo de datos y el oráculo.
- En una copia limpia (`git clone` + `python -m venv`) el componente funciona sin descarga adicional.
- Los motivos de rechazo se generan de forma completamente controlada, sin transformaciones implícitas de tipos.

**Desventajas:**
- Más líneas de código para operaciones que pandas hace en una sola expresión.
- Si el volumen de datos escala a millones de filas, el rendimiento puede ser inferior.

### B — pandas

**Ventajas:**
- Las operaciones de agrupación y conteo (`groupby`, `value_counts`) son concisas y rápidas.
- Mejor rendimiento con grandes volúmenes de datos gracias a operaciones vectorizadas.
- Menos código repetitivo para análisis y transformaciones.

**Desventajas (con honestidad):**
- Agrega una dependencia externa (`pip install pandas`), lo que complica reproducción
  en entornos sin acceso a red y aumenta el riesgo de conflictos de versión.
- La validación fila a fila con motivos exactos requiere iterar de todas formas
  (`iterrows` o `apply`), reduciendo la ventaja del enfoque vectorizado.
- El comportamiento ante tipos de datos ambiguos (fechas, vacíos) depende de las
  opciones de lectura de pandas, introduciendo posibles comportamientos implícitos
  difíciles de auditar en un piloto de calidad de datos.
- Mayor fricción en la reproducibilidad del piloto: `requirements.txt` más pesado.

---

## Propuesta recomendada

> **Alternativa A — biblioteca estándar** (puntaje ponderado: **440/500**).

**Justificación:** Los tres criterios de mayor peso (instalación, trazabilidad y
reproducibilidad, 75 % del total) favorecen ampliamente a A. El piloto maneja un
volumen pequeño de registros (20 filas sintéticas; proyección de pocos cientos en
producción), por lo que la ventaja de rendimiento de pandas (10 % del peso) no
justifica la dependencia adicional. La claridad del código y la auditabilidad
de las reglas son prioritarias para un piloto CMMI DEV v1.3.

Si el equipo decide otra alternativa, el cambio se documentará en este mismo
archivo con los campos "Decisor final" y "Fecha de confirmación" completados.

