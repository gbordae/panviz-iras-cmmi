# Guión de Validación Funcional — Usuario Simulado (E2 Meza Vizcarra, Cielo)

| Metadato         | Valor                                                    |
|------------------|----------------------------------------------------------|
| Rol validador    | E2 Meza Vizcarra, Cielo (Requisitos y usuario simulado)  |
| Versión evaluada | Línea base B2 / Componente v1 con CR01                   |
| Repositorio Git  | `https://github.com/gbordae/panviz-iras-cmmi.git`        |
| Commit validado  |                                                          |
| Fecha ejecución  |                                                          |

> **Nota metodológica obligatoria:** *La validación del usuario simulado no equivale a la aprobación de una autoridad sanitaria real ni a un aval clínico-epidemiológico oficial.* Se realiza exclusivamente como práctica de ingeniería de software CMMI DEV v1.3 (área VAL).

---

## 1. Procedimiento de Preparación del Entorno

1. Abrir PowerShell y ubicarse en un directorio temporal limpio de trabajo (fuera del repositorio actual):
   ```powershell
   cd $env:TEMP
   git clone https://github.com/gbordae/panviz-iras-cmmi.git validacion_panviz
   cd validacion_panviz
   git checkout feature/componente-iras
   ```
2. Crear y activar el entorno virtual local:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Instalar dependencias exactas:
   ```powershell
   python -m pip install -r requirements.txt
   ```
4. Configurar el acceso a módulos e invocar el sistema:
   ```powershell
   $env:PYTHONPATH = "src"
   ```

---

## 2. Matriz de Escenarios de Validación

| ID | Escenario | Comando a ejecutar | Resultado esperado (Oráculo) | Resultado observado | Decisión |
|:---:|:---|:---|:---|:---:|:---:|
| **V-01** | Ejecución estándar sin filtro | `python -m panviz --entrada datos\notificaciones_iras_sinteticas.csv --salida salida_v01` | `leidas: 20`, `aceptadas: 15`, `rechazadas: 5`, `suma_consolidado: 15`, `diferencia_reconciliacion: 0`. Archivo `rechazos.csv` con exactamente 5 filas rechazadas en índices de fila_datos 8, 11, 14, 17 y 19. | | |
| **V-02** | Filtro específico por distrito Cercado | `python -m panviz --entrada datos\notificaciones_iras_sinteticas.csv --salida salida_v02 --distrito Cercado` | `distrito_filtrado: Cercado`, `aceptadas_del_distrito: 6`, `suma_consolidado: 6`, `diferencia_reconciliacion: 0`. `consolidado.csv` con 6 casos (W43: 60+ [2]; W44: 5-14 [1], 60+ [1]; W45: 60+ [1], 5-14 [1]). Mismos 5 rechazos. | | |
| **V-03** | Filtro con normalización de espacios y mayúsculas (`" cayma "`) | `python -m panviz --entrada datos\notificaciones_iras_sinteticas.csv --salida salida_v03 --distrito " cayma "` | `distrito_filtrado: cayma`, `aceptadas_del_distrito: 5`, `suma_consolidado: 5`, `diferencia_reconciliacion: 0`. Coincidencia con 5 casos de Cayma del oráculo. Mismos 5 rechazos. | | |
| **V-04** | Filtro específico por distrito Yanahuara | `python -m panviz --entrada datos\notificaciones_iras_sinteticas.csv --salida salida_v04 --distrito Yanahuara` | `distrito_filtrado: Yanahuara`, `aceptadas_del_distrito: 4`, `suma_consolidado: 4`, `diferencia_reconciliacion: 0`. Coincidencia con 4 casos de Yanahuara del oráculo. Mismos 5 rechazos. | | |

---

## 3. Conclusión de la Validación
*(A completar por E2 al finalizar las pruebas)*
- **Decisión final:** 
- **Observaciones:** 
