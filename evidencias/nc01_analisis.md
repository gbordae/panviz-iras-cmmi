# Análisis de No Conformidad NC-01 — Reproducibilidad del Entorno

| Metadato  | Valor                                              |
|-----------|----------------------------------------------------|
| Fecha     | 2026-11-08                                         |
| Autor     | Gabriela Borda (E1 Coordinación y mejora)          |
| Estado    | diagnosticado                                      |

---

## 1. Discrepancia de versión de pytest y entorno de ejecución

### Hallazgo
En `evidencias/pruebas/pytest_v0.txt` quedó registrado:
```text
platform win32 -- Python 3.12.7, pytest-9.1.1, pluggy-1.6.0
Version: pytest 9.1.1
```
Mientras que en `evidencias/entorno.txt` y en `requirements.txt` la versión registrada para el entorno virtual (`.venv`) es:
```text
pytest==9.2.0
```

### Comprobación y comandos ejecutados
Se ejecutó la inspección cruzada entre el Python del entorno virtual (`.\.venv\Scripts\python.exe`) y el comando `python` invocado por defecto en la shell:

```powershell
.\.venv\Scripts\python.exe -c "import sys; print('sys.prefix:', sys.prefix)"
# Salida: sys.prefix: D:\Unsa\CaS\TrabajoParcial8\.venv

.\.venv\Scripts\python.exe -m pytest --version
# Salida: pytest 9.2.0

python -m pytest --version
# Salida: pytest 9.1.1
```

### Causa
El comando `python -m pytest` se ejecutó resolviendo el binario de Python global de la máquina (`C:\Users\LENOVO\AppData\Local\Programs\Python\Python312`), el cual tiene instalado `pytest 9.1.1`, en lugar de invocar explícitamente el intérprete del entorno virtual (`.\.venv\Scripts\python.exe`), el cual tiene `pytest 9.2.0`.

---

## 2. Codificación de `requirements.txt` (UTF-16 LE con BOM)

### Hallazgo
El archivo `requirements.txt` fue generado originalmente mediante redirección en PowerShell (`python -m pip freeze > requirements.txt`). En Windows PowerShell 5.1, la redirección `>` genera archivos en codificación UTF-16 LE con marca de orden de bytes (BOM `0xFF 0xFE`).

### Comprobación y comandos ejecutados
Inspección de los primeros 16 bytes del archivo:

```powershell
.\.venv\Scripts\python.exe -c "with open('requirements.txt', 'rb') as f: data = f.read(16); print('Primeros 16 bytes:', list(data)); print('Hex:', data.hex())"
```

**Salida obtenida:**
```text
Primeros 16 bytes: [255, 254, 99, 0, 111, 0, 108, 0, 111, 0, 114, 0, 97, 0, 109, 0]
Hex: fffe63006f006c006f00720061006d00
```

Los bytes `0xFF 0xFE` (`fffe`) confirman la presencia de BOM UTF-16 LE con caracteres codificados en 2 bytes (nótese el byte nulo `0x00` alternado). Esto puede generar incompatibilidades al ejecutar `pip install -r requirements.txt` en herramientas estándar que esperan UTF-8 sin BOM.

---

## 3. Conclusión y plan de acción
- Regenerar `requirements.txt` en UTF-8 sin BOM con fin de línea LF (`\n`), preservando exactamente las mismas versiones de paquetes.
- Realizar una verificación previa en copia limpia instalando en un entorno virtual temporal en `$env:TEMP` utilizando el Python del sistema y ejecutando la suite de pruebas desde ese entorno.
- Formalizar el hallazgo en `docs/gestion/nc01.md`.
