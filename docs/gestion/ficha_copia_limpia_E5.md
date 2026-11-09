# Ficha de Verificación Independiente en Copia Limpia — Baseline B1/B2

| Metadato                 | Valor                                                    |
|--------------------------|----------------------------------------------------------|
| Responsable verificación | E5 Ccoscco Alvis, Italo (Configuración y medición)       |
| Repositorio origen       | `https://github.com/gbordae/panviz-iras-cmmi.git`        |
| Carpeta de ejecución     | `D:\CaS_trabajo_08\copia_limpia`                         |
| Commit o tag clonado     | pendiente                                                |
| Fecha de verificación    | 2026-11-08                                               |
| Hora del mensaje         | 21:40 (Evidencia_09)                                     |
| Evidencias asociadas     | `evidencias/revisiones/Evidencia_09.png` y `evidencias/pruebaLimpia/PruebaLimpia.png` |

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
| **Python version (`python --version`)** | pendiente |
| **Intérprete / `sys.prefix`** | `D:\CaS_trabajo_08\copia_limpia\.venv` |
| **Resultado de pytest (esperado: 19 passed)** | pytest 9.2.0, 19 passed in 0.38s |
| **Resultado de ejecución CLI (resumen de salida_e5)** | leidas 20, aceptadas 15, rechazadas 5, suma 15, diferencia 0 |
| **Estado de verificación** | ejecutado en copia limpia sobre la rama |

## 3. Observaciones del Verificador (E5)

segun captura de E5
