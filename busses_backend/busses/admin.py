from django.contrib import admin

from .models import Bus, Route, ScheduleAssigment

admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(ScheduleAssigment)
