from django.contrib import admin

from .models import Bus, Chofer, Trayecto

admin.site.register(Bus)
admin.site.register(Trayecto)
admin.site.register(Chofer)
