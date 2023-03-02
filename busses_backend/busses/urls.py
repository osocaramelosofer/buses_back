from django.urls import path
from rest_framework import routers

from .api.views import ChoferModelViewSet, TrayectoModelViewSet

router = routers.SimpleRouter()
router.register(r"trayectos", TrayectoModelViewSet)
# router.register("chofers", ChoferModelViewSet) Esto no va aqui, va en config/api_router.py

app_name = "buses"
urlpatterns = [
    # path("routes/", RouteList.as_view(), name="routes-list"),
    # path("routes/<int:pk>/", RouteDetail.as_view(), name="route-detail"),
    # path("buses/", BusList.as_view(), name="bus-list"),
    # path("buses/<int:pk>/", BusDetail.as_view(), name="bus-detail"),
    # path("assignment/", ScheduleAssigmentList.as_view(), name="assignment-list"),
    # path(
    #     "assignment/<int:pk>/",
    #     ScheduleAssigmentDetail.as_view(),
    #     name="assignment-detail",
    # ),
]

urlpatterns += router.urls
