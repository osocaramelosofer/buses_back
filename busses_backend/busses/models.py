from django.db import models


class Trayecto(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.origen - self.destino}"


class Bus(models.Model):
    numero_placa = models.CharField(max_length=50, default=None, blank=True, null=True)
    capacidad = models.SmallIntegerField(default=0)
    chofer = models.OneToOneField(
        "Chofer", on_delete=models.CASCADE, default=None, blank=True, null=True
    )

    def __str__(self):
        return f"{self.id} - {self.chofer} - {self.numero_placa}"


class Chofer(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}"


# class Pasajero(models.Model):
#     nombre = models.CharField(max_length=100)
#     horario = models.ForeignKey('Horario', on_delete=models.CASCADE)
#     asiento = models.OneToOneField('Asiento', on_delete=models.CASCADE)
#
#
# class Asiento(models.Model):
#     numero = models.PositiveSmallIntegerField(unique=True)
#     estado = models.CharField(max_length=20)
#
#
class Horario(models.Model):
    fecha_salida = models.DateTimeField()
    fecha_llegada = models.DateTimeField()
    trayecto = models.ForeignKey(Trayecto, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
