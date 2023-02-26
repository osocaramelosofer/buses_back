from rest_framework import serializers

from ..models import Bus, BusAssignment, Driver, Passenger, Route


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ["name", "seat_number"]


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ["name"]


class BusSerializer(serializers.ModelSerializer):
    bus_assignment = serializers.StringRelatedField(many=True)

    class Meta:
        model = Bus
        fields = ["serial_number", "capacity", "bus_assignment"]


class RouteSerializer(serializers.ModelSerializer):
    bus_assignment = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Route
        fields = [
            "name",
            "origin",
            "destination",
            "bus_assignment",
            "departure_date",
            "arrival_date",
        ]


class BusAssignmentSerializer(serializers.ModelSerializer):
    # route_name = serializers.CharField(source="route.name", read_only=True)
    # bus_serial_number = serializers.CharField(
    #     source="bus.serial_number", read_only=True
    # )
    route = serializers.StringRelatedField()
    bus = serializers.StringRelatedField()
    driver = serializers.StringRelatedField()
    passengers = PassengerSerializer(many=True, read_only=True)

    class Meta:
        model = BusAssignment
        fields = ["id", "route", "driver", "bus", "departure_date", "passengers"]
