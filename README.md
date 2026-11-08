# Panviz — Piloto CMMI DEV v1.3

## Objetivo del piloto

El presente piloto aplica el modelo CMMI DEV v1.3 al sistema Panviz, una solución de vigilancia epidemiológica de Infecciones Respiratorias Agudas Severas (IRAS). El objetivo es institucionalizar prácticas de ingeniería de software (requisitos, planificación, aseguramiento de calidad, control de configuración y medición) a través de un ciclo piloto controlado de siete fases, generando evidencias trazables que demuestren la madurez del proceso y la mejora continua del equipo de desarrollo.

## Estructura de carpetas

```
TrabajoParcial8/
├── src/                    # Código fuente del sistema
├── tests/                  # Pruebas unitarias y de integración
├── datos/                  # Conjuntos de datos de prueba y referencia
├── docs/
│   ├── proceso/            # Documentos de proceso (planes, procedimientos)
│   ├── requisitos/         # Especificaciones y casos de uso
│   └── gestion/            # Gestión del proyecto (equipo, cronograma, cambios)
├── evidencias/             # Evidencias CMMI (índice, entorno, registros)
├── .gitignore
├── requirements.txt
└── README.md
```

## Comandos de referencia

```bash
# Crear entorno virtual
python -m venv .venv

# Instalar dependencias
python -m pip install pytest

# Ejecutar pruebas unitarias y de integración
python -m pytest -q -v
```

## Uso

```powershell
# PowerShell — desde la raíz del proyecto
$env:PYTHONPATH = "src"
python -m panviz --entrada datos\notificaciones_iras_sinteticas.csv --salida evidencias\ejecucion_v0
```

## Estado

**Verificado por pruebas (PR-01 a PR-06) en rama `feature/componente-iras`, pendiente de revisión de código (B1)**

