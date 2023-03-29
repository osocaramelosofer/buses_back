from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CorridaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "busses_backend.corrida"
    verbose_name = _("Corridas")
