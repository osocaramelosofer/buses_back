from django.db import models


class Trayecto(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.origen} - {self.destino}"


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


class Boleto(models.Model):
    pasajero = models.OneToOneField("Pasajero", on_delete=models.CASCADE)
    asiento = models.OneToOneField("Asiento", on_delete=models.CASCADE)
    # bus = models.ForeignKey('Bus', on_delete=models.CASCADE) no lo necesitas aqui
    corrida = models.ForeignKey("Corrida", on_delete=models.CASCADE)

    def __str__(self):
        return f"Asiento: {self.asiento} | pasajero:{self.pasajero.nombre}"


class Pasajero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} "


class Asiento(models.Model):
    numero = models.PositiveSmallIntegerField()
    estado = models.CharField(max_length=20)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)


class Corrida(models.Model):
    fecha_salida = models.DateTimeField()
    fecha_llegada = models.DateTimeField()
    trayecto = models.ForeignKey(Trayecto, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    # capacidad = models.SmallIntegerField(default=0)

    def __str__(self):
        return f"Trayecto:{self.trayecto} | Bus info: {self.bus}"
