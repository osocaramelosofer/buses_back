from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from busses_backend.busses.models import Corrida
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
