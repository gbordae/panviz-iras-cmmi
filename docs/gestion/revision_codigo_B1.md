# Revisión de Código Baseline B1 — Componente Panviz IRAS

| Campo                 | Valor                                         |
|-----------------------|-----------------------------------------------|
| **Producto revisado** | `src/panviz/` (commit a090c29)                |
| **Autor (rol)**       | E3 Fernandez Huarca, Rodrigo (Diseño y desarrollo) |
| **Revisor**           |                                               |
| **Fecha**             |                                               |
| **Decisión**          |                                               |
| **Cierre**            |                                               |

---

## Lista de revisión general

| Ítem                      | ¿Revisado? | Hallazgos |
|---------------------------|------------|-----------|
| Requisitos                | ☐          |           |
| Diseño                    | ☐          |           |
| Código                    | ☐          |           |
| Pruebas                   | ☐          |           |
| Liberación / trazabilidad | ☐          |           |

---

## Lista de chequeo técnica para el Revisor (E4 Calidad y pruebas)

- [ ] Cada regla de validación del diseño está implementada en el código (`src/panviz/validador.py`).
- [ ] Los motivos de rechazo son exactamente los literales del diseño:
  - `"campo obligatorio vacio (<campo>)"`
  - `"fecha imposible"`
  - `"evento distinto de IRAS"`
  - `"grupo etario fuera de catalogo"`
  - `"clave duplicada"`
- [ ] Manejo estricto del contrato de columnas: verifica orden y nombres exactos en `src/panviz/importador.py`.
- [ ] Manejo correcto de códigos de salida: código 2 por contrato inválido y código 3 por falla de reconciliación.
- [ ] Funciones pequeñas, modulares y con docstring conciso.
- [ ] Cero datos o valores del oráculo codificados en duro dentro de `src/panviz/`.
- [ ] El consolidador (`src/panviz/consolidador.py`) está diseñado como función pura sin efectos colaterales.

---

## Hallazgos y acciones

_(Se completará por el revisor E4 durante la sesión de revisión)_

| ID | Archivo / Línea | Descripción del hallazgo | Acción requerida | Responsable | Estado |
|----|-----------------|--------------------------|------------------|-------------|--------|
|    |                 |                          |                  |             |        |
