from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BussesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "busses_backend.busses"
    verbose_name = _("Buses")
