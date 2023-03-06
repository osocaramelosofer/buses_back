from django.db import DatabaseError, transaction
from rest_framework import serializers

from ..models import Asiento, Bus, Chofer, Pasajero, Trayecto


class PasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasajero
        fields = ["nombre"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["id"] = instance.id
        return data


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

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["id"] = instance.id
        return data


class BusSerializer(serializers.ModelSerializer):
    chofer = ChoferSerializer()

    class Meta:
        model = Bus
        fields = ["numero_placa", "chofer", "capacidad"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["id"] = instance.id
        return data

    def create(self, validated_data):
        chofer = validated_data.pop("chofer")

        bus_instance = Bus.objects.create(**validated_data)

        if chofer:
            chofer_instance = Chofer.objects.create(**chofer)
            bus_instance.chofer = chofer_instance
            bus_instance.save()

        # Create seats
        print("======= Creating seats =======")
        seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        seatsSerialized = []
        try:
            with transaction.atomic():
                print("======= Before for =======")
                for seat_number in seats:
                    print("======= Inside for =======")
                    seat_instance = Asiento.objects.create(
                        bus=bus_instance, numero=seat_number, estado="disponible"
                    )
                    print(
                        "======= Seat Created =======",
                        AsientoSerializer(seat_instance).data,
                    )
                    seatsSerialized.append(AsientoSerializer(seat_instance).data)

        except DatabaseError as err:
            print(err)

        return bus_instance


class AsientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asiento
        fields = ["bus", "numero", "estado"]


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
