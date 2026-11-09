# Lineas Base del Piloto Panviz IRAS

| Metadato    | Valor                                              |
|-------------|--------------------------------------------------|
| Autor       | E1 Borda Espinoza Gabriela (Coordinacion y mejora) |
| Fecha       | 2026-11-09                                        |
| Hora        | 15:34                                         |

---

## B0 - Linea Base de Requisitos (v0.2)

| Campo                  | Valor |
|------------------------|-------|
| **ID linea base**      | B0 |
| **Producto**           | `docs/requisitos/requisitos.md` (v0.2) |
| **Aprobador**          | E1 Borda Espinoza Gabriela |
| **Fecha de aprobacion**| 2026-11-09 (fecha real de registro) |
| **Hora de registro**   | 15:34 |
| **Estado**             | aprobada |
| **Nota**               | decision comunicada por E1 el 2026-11-08 ~22:40 segun E1; sin registro previo en el repositorio; registrada el 2026-11-09 15:34:09 |
| **Pendiente**          | Confirmacion de E3 sobre v0.2 (Evidencia de E3 sobre requisitos v0.2 no archivada) |

### Artefactos incluidos en B0

| Artefacto | Ruta |
|-----------|------|
| Requisitos v0.2 | `docs/requisitos/requisitos.md` |
| Catalogo de datos | `docs/requisitos/catalogo_datos.md` |

---

## B1 - Linea Base del Codigo (feature/componente-iras)

| Campo                  | Valor |
|------------------------|-------|
| **ID linea base**      | B1 |
| **Producto**           | `src/panviz/` (rama feature/componente-iras) |
| **Commit de referencia**| b23b4ee (HEAD de feature/componente-iras al momento de registro) |
| **Commit de CR01 aprobado** | be0f464 (implementacion de CR01 aprobada por E1 en f9f8d03) |
| **Aprobador**          | E1 Borda Espinoza Gabriela |
| **Fecha de aprobacion**| 2026-11-09 |
| **Estado**             | aprobada |
| **Pendiente**          | Captura formal del PR de E4 sobre CR01 (Evidencia_06: hora y commit revisado pendientes) |

---

## B2 - Linea Base de Validacion

| Campo                  | Valor |
|------------------------|-------|
| **ID linea base**      | B2 |
| **Producto**           | Componente Panviz IRAS validado funcionalmente |
| **Commit validado**    | c7989fb (commit validado por E2 Meza Vizcarra Cielo) |
| **Acta de validacion** | `docs/gestion/acta_validacion_B2.md` |
| **Confirmacion de E2** | confirmada (Evidencia_11, 2026-11-09 14:07) |
| **Copia limpia E5**    | `evidencias/pruebaLimpia/PruebaLimpia_02.png` (commit c7989fb, Python 3.12.7) |
| **git diff c7989fb HEAD -- src tests** | sin cambios (src/ y tests/ identicos) |
| **Aprobador**          | E1 Borda Espinoza Gabriela |
| **Fecha de aprobacion**| 2026-11-09 |
| **Estado**             | aprobada (acta confirmada por E2 y copia limpia valida para el codigo actual) |
| **Pendiente**          | Captura formal del PR de E4 sobre CR01 (Evidencia_06 sin hora ni commit revisado) |

---

> **Nota:** Las lineas base B1 y B2 seran actualizadas con el hash del tag v0.1 tras
> la fusion a main. Ver seccion de liberacion en `docs/gestion/registro_revisiones.csv`.
