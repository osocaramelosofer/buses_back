from rest_framework import status, viewsets
from rest_framework.response import Response

from ..models import Asiento, Boleto, Bus, Chofer, Pasajero, Trayecto
from .serializers import (
    AsientoSerializer,
    BoletoSerializer,
    BusSerializer,
    ChoferSerializer,
    PasajeroSerializer,
    TrayectoSerializer,
)


class TrayectoModelViewSet(viewsets.ModelViewSet):
    queryset = Trayecto.objects.all()
    serializer_class = TrayectoSerializer


class ChoferModelViewSet(viewsets.ModelViewSet):
    queryset = Chofer.objects.all()
    serializer_class = ChoferSerializer
    http_method_names = ["get", "delete", "put"]

    def destroy(self, request, *args, **kwargs):
        chofer_instance = self.get_object()
        chofer_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BusModelViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class PasajeroModelViewSet(viewsets.ModelViewSet):
    queryset = Pasajero.objects.all()
    serializer_class = PasajeroSerializer


class AsientoModelViewSet(viewsets.ModelViewSet):
    queryset = Asiento.objects.all()
    serializer_class = AsientoSerializer


class BoletoModelViewSet(viewsets.ModelViewSet):
    queryset = Boleto.objects.all()
    serializer_class = BoletoSerializer
