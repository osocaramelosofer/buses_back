from django.db import DatabaseError, transaction
from rest_framework import serializers

from ..models import Asiento, Boleto, Bus, Chofer, Corrida, Pasajero, Trayecto


class PasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasajero
        fields = ["nombre"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["id"] = instance.id
        return data


class ChoferSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Chofer
        fields = ["id", "nombre"]

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
            try:
                obj = Chofer.objects.get(id=chofer["id"])
                bus_instance.chofer = obj
                bus_instance.save()
            except Chofer.DoesNotExist:
                chofer_instance = Chofer.objects.create(**chofer)
                bus_instance.chofer = chofer_instance
                bus_instance.save()

        # Create seats for each buss
        seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        try:
            with transaction.atomic():
                for seat_number in seats:
                    Asiento.objects.create(
                        bus=bus_instance, numero=seat_number, estado="disponible"
                    )
        except DatabaseError as err:
            print(err)

        return bus_instance


class AsientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asiento
        fields = ["bus", "numero", "estado"]


class BoletoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleto
        fields = "__all__"

    # def create(self, validated_data):
    #     print("+++++ DATA ++++++",validated_data)
    #     asiento = validated_data.pop('asiento')
    #     corrida = validated_data.pop('corrida')
    #     pasajero = validated_data.pop('pasajero')
    #
    #
    #     asiento_obj = Asiento.objects.filter(pk=asiento).first()
    #     pasajero_obj = Pasajero.objects.filter(pk=pasajero).first()
    #     corrida_obj = Corrida.objects.filter(pk=corrida).first()
    #
    #
    #     with transaction.atomic():
    #         asiento_obj.estado = "ocupado"
    #         asiento_obj.save()
    #         Boleto.objects.create(asiento=asiento_obj, pasajero=pasajero_obj, corrida=corrida_obj)


class CorridaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corrida
        fields = "__all__"
