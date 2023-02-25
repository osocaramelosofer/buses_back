from django.urls import path

from .api.views import (
    BusDetail,
    BusList,
    RouteDetail,
    RouteList,
    ScheduleAssigmentDetail,
    ScheduleAssigmentList,
)

app_name = "buses"
urlpatterns = [
    path("routes/", RouteList.as_view(), name="routes-list"),
    path("routes/<int:pk>/", RouteDetail.as_view(), name="route-detail"),
    path("buses/", BusList.as_view(), name="bus-list"),
    path("buses/<int:pk>/", BusDetail.as_view(), name="bus-detail"),
    path("assignment/", ScheduleAssigmentList.as_view(), name="assignment-list"),
    path(
        "assignment/<int:pk>/",
        ScheduleAssigmentDetail.as_view(),
        name="assignment-detail",
    ),
]
