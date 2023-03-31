from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BoletosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'busses_backend.boletos'
    verbose_name = _("Boletos")

