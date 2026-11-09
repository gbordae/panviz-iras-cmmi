# Registro de Revisión Formal de Código — Línea Base B1

| Metadato              | Valor                                                                 |
|-----------------------|-----------------------------------------------------------------------|
| **Tipo de revisión**  | Revisión por pares (Peer Review) — Inspección de código               |
| **Proceso asociado**  | CMMI-DEV v1.3 — Verificación (VER) / SP 2.1, 2.2, 2.3                 |
| **Línea base**        | B1 — Componente Panviz IRAS y Solicitud de Cambio CR01                |
| **Fecha de registro** | 2026-11-08                                                            |
| **Autor del registro**| E1 Borda Espinoza, Gabriela (Coordinación y mejora)                   |

---

## 1. Alcance de la Revisión

La revisión de código de la línea base B1 abarca:
1. **Código base v0 (`src/panviz/`):** Implementación de los módulos de ingesta, validación, consolidación y exportación de notificaciones epidemiológicas IRAS.
2. **Código incremental de CR01 (`src/panviz/filtro.py`, `src/panviz/cli.py`, `src/panviz/exportador.py`):** Modificaciones para soportar el filtro opcional por distrito, normalización de cadenas de texto y extensión de los metadatos de reconciliación en el resumen.

---

## 2. Registros de Revisión por Pares

### 1. Revisión del Código Base v0

| Campo                 | Valor                                                         |
|-----------------------|---------------------------------------------------------------|
| **Producto revisado** | Módulos v0 en `src/panviz/` (`lector.py`, `validador.py`, `consolidador.py`, `exportador.py`, `cli.py`) |
| **Commit revisado**   | `be0f464`                                                     |
| **Autor (rol)**       | E3 Fernandez Huarca, Rodrigo (Diseño y desarrollo)            |
| **Revisor**           | E4 Suclle Suca, Michael (Calidad y pruebas)                   |
| **Fecha y hora**      | 2026-11-08 17:22 (Evidencia_02)                               |
| **Evidencia**         | `evidencias/revisiones/Evidencia_02.png`                      |
| **Decisión**          | Aprobado                                                      |
| **Hallazgos**         | Sin hallazgos bloqueantes                                     |

---

### 2. Revisión del Código Incremental de CR01 (Filtro por Distrito)

| Campo                 | Valor                                                         |
|-----------------------|---------------------------------------------------------------|
| **Producto revisado** | Código incremental de CR01 (`src/panviz/filtro.py`, `src/panviz/cli.py`, `src/panviz/exportador.py`) |
| **Commit revisado**   | pendiente de verificar según el PR                            |
| **Autor (rol)**       | E3 Fernandez Huarca, Rodrigo (Diseño y desarrollo)            |
| **Revisor**           | E4 Suclle Suca, Michael (Calidad y pruebas)                   |
| **Fecha y hora**      | pendiente de archivar                                         |
| **Evidencia**         | captura pendiente de archivar en evidencias/revisiones/       |
| **Decisión**          | pendiente de verificación de evidencia                         |
| **Hallazgos**         | ver comentarios del Pull Request                              |

---

## 3. Estado de Consolidación

- **Cobertura de código base v0:** Aprobada y respaldada en `evidencias/revisiones/Evidencia_02.png`.
- **Cobertura de cambios CR01:** Pendiente de archivar la captura de aprobación del PR en `evidencias/revisiones/`.
- **Estado general en `docs/gestion/registro_revisiones.csv`:** `parcial: aprobacion de E4 sobre CR01 sin captura archivada`.
