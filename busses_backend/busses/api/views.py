from rest_framework import generics

from ..models import Bus, Route, ScheduleAssigment
from .serializers import BusSerializer, RouteSerializer, ScheduleAssigmentSerializer


class RouteList(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class RouteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class BusList(generics.ListCreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class BusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class ScheduleAssigmentList(generics.ListCreateAPIView):
    queryset = ScheduleAssigment.objects.all()
    serializer_class = ScheduleAssigmentSerializer


class ScheduleAssigmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScheduleAssigment.objects.all()
    serializer_class = ScheduleAssigmentSerializer
