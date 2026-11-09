# Revisión de Código Baseline B1 — Componente Panviz IRAS

| Campo                 | Valor                                         |
|-----------------------|-----------------------------------------------|
| **Producto revisado** | `src/panviz/` (commit revisado: "[completar segun el PR]") |
| **Autor (rol)**       | E3 Fernandez Huarca, Rodrigo (Diseño y desarrollo) |
| **Revisor**           | E4 Suclle Suca, Michael (Calidad y pruebas)   |
| **Fecha**             | 2026-11-08 (hora segun la captura: "[completar]") |
| **Decisión**          | aprobado en Pull Request (ver Evidencia_02)   |
| **Cierre**            | Evidencia_02 (Pull Request aprobado en GitHub)|

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

ver comentarios del Pull Request

| ID | Archivo / Línea | Descripción del hallazgo | Acción requerida | Responsable | Estado |
|----|-----------------|--------------------------|------------------|-------------|--------|
|    |                 |                          |                  |             |        |

