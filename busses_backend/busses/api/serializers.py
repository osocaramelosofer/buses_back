from rest_framework import serializers

from ..models import Bus, Chofer, Trayecto

# class PassengerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Passenger
#         fields = ["name", "seat_number"]
#
#


class ChoferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chofer
        fields = ["nombre"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["id"] = instance.id
        return data


class TrayectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trayecto
        fields = ["origen", "destino"]


class BusSerializer(serializers.ModelSerializer):
    chofer = ChoferSerializer()

    class Meta:
        model = Bus
        fields = ["numero_placa", "chofer", "capacidad"]

    def create(self, validated_data):
        chofer = validated_data.pop("chofer")

        bus_instance = Bus.objects.create(**validated_data)

        if chofer:
            chofer_instance = Chofer.objects.create(**chofer)
            bus_instance.chofer = chofer_instance
            bus_instance.save()

        return bus_instance


# class RouteSerializer(serializers.ModelSerializer):
#     bus_assignment = serializers.StringRelatedField(many=True, read_only=True)
#
#     class Meta:
#         model = Route
#         fields = [
#             "name",
#             "origin",
#             "destination",
#             "bus_assignment",
#             "departure_date",
#             "arrival_date",
#         ]
#
#
# class BusAssignmentSerializer(serializers.ModelSerializer):
#     route = serializers.StringRelatedField()
#     bus = serializers.StringRelatedField()
#     driver = serializers.StringRelatedField()
#     passengers = PassengerSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = BusAssignment
#         fields = ["id", "route", "driver", "bus", "departure_date", "passengers", "arrival_date"]
