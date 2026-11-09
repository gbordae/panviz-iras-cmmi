# Ficha de Verificación Independiente en Copia Limpia — Baseline B1/B2

| Metadato                 | Valor                                                    |
|--------------------------|----------------------------------------------------------|
| Responsable verificación | E5 Ccoscco Alvis, Italo (Configuración y medición)       |
| Repositorio origen       | `https://github.com/gbordae/panviz-iras-cmmi.git`        |
| Commit o tag clonado     |                                                          |
| Fecha de verificación    |                                                          |

---

## 1. Instrucciones de Ejecución para E5

1. Clonar en una carpeta nueva completamente aislada:
   ```powershell
   cd $env:TEMP
   git clone https://github.com/gbordae/panviz-iras-cmmi.git panviz_copia_limpia_e5
   cd panviz_copia_limpia_e5
   git checkout feature/componente-iras
   ```
2. Crear un entorno virtual limpio e instalar dependencias:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   ```
3. Ejecutar suite automatizada de pruebas y registrar salida:
   ```powershell
   python -m pytest -q
   ```
4. Ejecutar prueba de humo del componente CLI:
   ```powershell
   $env:PYTHONPATH = "src"
   python -m panviz --entrada datos\notificaciones_iras_sinteticas.csv --salida salida_limpia_e5
   ```

---

## 2. Registro de Datos de Verificación (A completar por E5)

| Parámetro | Valor observado |
|---|---|
| **Python version (`python --version`)** | |
| **Intérprete / `sys.prefix`** | |
| **Resultado de pytest (esperado: 19 passed)** | |
| **Resultado de ejecución CLI** | |
| **Estado de verificación** | |

## 3. Observaciones del Verificador (E5)
