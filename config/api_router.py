from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from busses_backend.busses.api.views import (
    AsientoModelViewSet,
    BoletoModelViewSet,
    BoletoViewSet,
    BusModelViewSet,
    ChoferModelViewSet,
    CorridaModelViewSet,
    CreateBoletoGenericApiView,
    PasajeroModelViewSet,
    TrayectoModelViewSet,
    CreateBusGenericApiView
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
router.register("boletos-modelviewset", BoletoModelViewSet)
router.register("boletos-viewset", BoletoViewSet)
router.register("corridas", CorridaModelViewSet)


app_name = "api"
urlpatterns = [
    path("crear-boleto", CreateBoletoGenericApiView.as_view()),
    path("crear-bus", CreateBusGenericApiView.as_view()),
]
urlpatterns += router.urls
# urlpatterns += busurls
