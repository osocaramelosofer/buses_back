from django.db import models


class Route(models.Model):
    name = models.CharField(max_length=200)
    origin = models.FloatField()
    duration = models.FloatField()
    destination = models.CharField(max_length=100)
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Bus(models.Model):
    serial_number = models.CharField(max_length=255)
    capacity = models.PositiveSmallIntegerField(default=10)

    def __str__(self):
        return f"Bus {self.id} - serial number {self.serial_number}"


class Driver(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class BusAssignment(models.Model):
    route = models.ForeignKey(
        Route, on_delete=models.CASCADE, related_name="bus_assignment"
    )
    bus = models.ForeignKey(
        Bus, on_delete=models.CASCADE, related_name="bus_assignment"
    )
    driver = models.ForeignKey(
        Driver, on_delete=models.CASCADE, related_name="bus_assignment"
    )
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()

    def __str__(self):
        return f"{self.route.name} - {self.bus.serial_number}"


class Passenger(models.Model):
    name = models.CharField(max_length=50)
    seat_number = models.IntegerField()
    bus_assignment = models.ForeignKey(
        BusAssignment, on_delete=models.CASCADE, related_name="passengers"
    )
