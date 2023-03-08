from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from busses_backend.busses.api.views import (
    AsientoModelViewSet,
    BoletoModelViewSet,
    BusModelViewSet,
    ChoferModelViewSet,
    PasajeroModelViewSet,
    TrayectoModelViewSet,
)
# from busses_backend.busses.urls import urlpatterns as busurls
from busses_backend.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("trayectos", TrayectoModelViewSet)
router.register("chofers", ChoferModelViewSet)
router.register("buses", BusModelViewSet)
router.register("pasajeros", PasajeroModelViewSet)
router.register("asientos", AsientoModelViewSet)
router.register("boletos", BoletoModelViewSet)

app_name = "api"
urlpatterns = router.urls
# urlpatterns += busurls
