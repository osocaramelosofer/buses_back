from rest_framework import serializers
from busses_backend.busses.models import Corrida
from busses_backend.busses.api.serializers import BusSerializer, TrayectoSerializer


class ReadCorridaSerializer(serializers.ModelSerializer):
    bus = BusSerializer()
    trayecto = TrayectoSerializer()

    class Meta:
        model = Corrida
        fields = ['id','fecha_salida','fecha_llegada','bus','trayecto']
