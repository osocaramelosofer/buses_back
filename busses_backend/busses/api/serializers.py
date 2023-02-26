from rest_framework import serializers

from ..models import Bus, BusAssignment, Route


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = "__all__"


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = "__all__"


class ScheduleAssigmentSerializer(serializers.ModelSerializer):
    route_name = serializers.CharField(source="route.name", read_only=True)
    bus_serial_number = serializers.CharField(
        source="bus.serial_number", read_only=True
    )

    class Meta:
        model = BusAssignment
        fields = ["id", "route", "route_name", "bus", "bus_serial_number", "schedule"]
