from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from django.db import DatabaseError, transaction

from busses_backend.busses.models import Corrida, Bus, Trayecto

from .serializers import ReadCorridaSerializer


class ItemViewSet(ViewSet):
    queryset = Corrida.objects.all()

    def list(self, request):
        serializer = ReadCorridaSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = ReadCorridaSerializer(item)
        return Response(serializer.data, status=200)

    def put(self, request, *args, **kwargs):

        bus_id = request.data.pop('bus')
        trayecto_id = request.data.pop('trayecto')
        corrida_id = request.data.pop('id')
        fecha_salida = request.data.pop('fecha_salida')
        fecha_llegada = request.data.pop('fecha_llegada')

        updated_bus = Bus.objects.filter(pk=bus_id).first()
        updated_trayecto = Trayecto.objects.filter(pk=trayecto_id).first()
        current_corrida = Corrida.objects.filter(pk=corrida_id).first()

        if current_corrida:
            with transaction.atomic():
                current_corrida.bus = updated_bus
                current_corrida.trayecto = updated_trayecto
                current_corrida.fecha_salida = fecha_salida
                current_corrida.fecha_llegada = fecha_llegada
                current_corrida.save()
                corrida_instance = ReadCorridaSerializer(current_corrida).data

                return Response(
                    {
                        "message": "Datos actualizados exitosamente.",
                        "bus": corrida_instance,
                    },
                    status=status.HTTP_200_OK,
                )
        return Response(
            {
                "message": "Hubo un problema actualizando los datos.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
