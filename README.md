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

# Ejecutar pruebas en modo silencioso
python -m pytest -q
```

## Estado

**En construcción**

