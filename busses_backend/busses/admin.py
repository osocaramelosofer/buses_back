from django.contrib import admin

from .models import Bus, BusAssignment, Route

admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(BusAssignment)
