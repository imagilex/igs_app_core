# igs-app-core

Un paquete Django reusable que funciona como aplicación instalable con `pip install` desde GitHub.

## Instalación

Instala localmente para desarrollo:

```bash
python -m pip install -e .
```

Instala desde GitHub:

```bash
python -m pip install git+https://github.com/imagilex/igs_app_core.git
```

## Uso

Agrega la app a `INSTALLED_APPS` en tu proyecto Django:

```python
INSTALLED_APPS = [
    # ... otras apps
    "igs_app_core",
]
```

Incluye sus URLs en `urls.py`:

```python
from django.urls import include, path

urlpatterns = [
    path("core/", include("igs_app_core.urls")),
]
```

Accede a la vista de ejemplo en `http://localhost:8000/core/`.

## Estructura

- `igs_app_core/` – paquete Django reusable.
- `example_project/` – proyecto Django de ejemplo para pruebas.

## Publicar en GitHub

1. Crea un repo en GitHub llamado `igs_app_core`.
2. Sube este código.
3. Instala con `pip install git+https://github.com/<tu_usuario>/igs_app_core.git`.


1. Crea un repo en GitHub llamado `igs_app_core`.
2. Sube este código.
3. Instala con `pip install git+https://github.com/<tu_usuario>/igs_app_core.git`.
>>>>>>> 87ea9c4 (Commit inicial: estructura base de la app reusable Django)
