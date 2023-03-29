from django.db import DatabaseError, transaction
from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from ..models import Asiento, Boleto, Bus, Chofer, Corrida, Pasajero, Trayecto
from .serializers import (
    AsientoSerializer,
    BoletoSerializer,
    BusSerializer,
    ChoferSerializer,
    CorridaSerializer,
    FullBoletosSerializer,
    FullCorridaSerializer,
    PasajeroSerializer,
    TrayectoSerializer,
)


class TrayectoModelViewSet(viewsets.ModelViewSet):
    queryset = Trayecto.objects.all()
    serializer_class = TrayectoSerializer


class ChoferModelViewSet(viewsets.ModelViewSet):
    queryset = Chofer.objects.all()
    serializer_class = ChoferSerializer
    http_method_names = ["get", "delete", "put", "post"]

    def destroy(self, request, *args, **kwargs):
        chofer_instance = self.get_object()
        chofer_instance.delete()
        return Response(
            {"data": "Conductor eliminado correctamente"},
            status=status.HTTP_204_NO_CONTENT,
        )


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


class BoletoViewSet(ViewSet):
    queryset = Boleto.objects.all()

    def list(self, request):
        serializer = BoletoSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = BoletoSerializer(item)
        return Response(serializer.data)


class CreateBoletoGenericApiView(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView,
):
    serializer_class = BoletoSerializer
    queryset = Boleto.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "POST":
            return FullBoletosSerializer
        return BoletoSerializer.default

    def post(self, request, *args, **kwargs):
        asiento = request.data.pop("asiento")
        asiento_instance = Asiento.objects.filter(
            numero=asiento.get("numero"), bus=asiento.get("bus")
        ).first()

        pasajero = request.data.pop("pasajero")
        pasajero_instance = Pasajero.objects.filter(pk=pasajero.get("id")).first()

        corrida = request.data.pop("corrida")
        corrida_instance = Corrida.objects.filter(pk=corrida).first()

        try:
            with transaction.atomic():
                asiento_instance.estado = "ocupado"
                asiento_instance.save()
                boleto = Boleto.objects.create(
                    pasajero=pasajero_instance,
                    asiento=asiento_instance,
                    corrida=corrida_instance,
                )
                serializer = self.get_serializer(boleto)
                headers = self.get_success_headers(serializer.data)
                return Response(
                    {
                        "message": "Boleto comprado exitosamente.",
                        "data": serializer.data,
                    },
                    status=status.HTTP_201_CREATED,
                    headers=headers,
                )
        except DatabaseError as err:
            return Response(
                {
                    "message": "Error al intentar crear el objecto boleto",
                    "error": True,
                    "code": 500,
                }
            )


class CorridaModelViewSet(viewsets.ModelViewSet):
    queryset = Corrida.objects.all()
    serializer_class = CorridaSerializer


class CreateBusGenericApiView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView,
):
    serializer_class = BusSerializer
    queryset = Bus.objects.all()
    http_method_names = ["put", "post"]

    def put(self, request, *args, **kwargs):
        print("Request DATA", request.data)
        bus = request.data.pop("bus")
        chofer = request.data.pop("chofer")
        # print("CHOFER_ID", chofer.get("id"))
        chofer = Chofer.objects.filter(pk=chofer.get("id")).first()
        old_bus = Bus.objects.filter(pk=bus.get("id")).first()

        busUpdated = None
        if chofer and old_bus:
            with transaction.atomic():
                old_bus.numero_placa = bus.get("numero_placa")
                old_bus.capacidad = bus.get("capacidad")
                old_bus.chofer = chofer
                old_bus.save()
                busUpdated = BusSerializer(old_bus).data
                print("bus udpated ============", busUpdated)

        return Response(
            {
                "message": "Boleto comprado exitosamente.",
                "bus": busUpdated,
            },
            status=status.HTTP_201_CREATED,
        )
