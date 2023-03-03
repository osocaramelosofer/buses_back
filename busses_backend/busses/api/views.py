from rest_framework import status, viewsets
from rest_framework.response import Response

from ..models import Bus, Chofer, Trayecto
from .serializers import BusSerializer, ChoferSerializer, TrayectoSerializer


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
