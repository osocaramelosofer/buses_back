from django.db import DatabaseError, transaction
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from busses_backend.busses.models import Boleto, Asiento

from busses_backend.busses.api.serializers import AsientoSerializer


class AsientosViewSet(ViewSet):
    queryset = Asiento.objects.all()

    def list(self, request, *args, **kwargs):
        bus_id = request.query_params.get('bus')
        queryset = Asiento.objects.filter(bus_id=bus_id)
        asientos = AsientoSerializer(queryset, many=True)

        return Response(asientos.data, status=200)
