from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from busses_backend.busses.urls import urlpatterns as busurls
from busses_backend.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls
urlpatterns += busurls
