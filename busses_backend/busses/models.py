from django.db import models


class Route(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()

    def __str__(self):
        return self.name


class Bus(models.Model):
    serial_number = models.CharField(max_length=255)
    capacity = models.PositiveSmallIntegerField(default=10)


class ScheduleAssigment(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    schedule = models.DateTimeField()

    def __str__(self):
        return f"{self.route.name} - {self.bus.serial_number} - {self.schedule}"
