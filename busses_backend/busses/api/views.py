from rest_framework import generics, viewsets

from ..models import Bus, Chofer, Trayecto
from .serializers import BusSerializer, ChoferSerializer, TrayectoSerializer


class TrayectoModelViewSet(viewsets.ModelViewSet):
    queryset = Trayecto.objects.all()
    serializer_class = TrayectoSerializer


class ChoferModelViewSet(viewsets.ModelViewSet):
    queryset = Chofer.objects.all()
    serializer_class = ChoferSerializer


class BusModelViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
