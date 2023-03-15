<<<<<<<< HEAD:app/backend/apps.py
from django.apps import AppConfig


class BackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend'
========
from django.apps import AppConfig


class FrontendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'frontend'
>>>>>>>> b4b5c7e (update project):app/frontend/apps.py
