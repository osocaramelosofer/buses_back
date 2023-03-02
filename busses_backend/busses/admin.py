from django.contrib import admin

from .models import Asiento, Boleto, Bus, Chofer, Corrida, Pasajero, Trayecto

admin.site.register(Bus)
admin.site.register(Trayecto)
admin.site.register(Chofer)
admin.site.register(Corrida)
admin.site.register(Pasajero)
admin.site.register(Boleto)
admin.site.register(Asiento)
