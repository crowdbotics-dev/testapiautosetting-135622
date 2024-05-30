from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors135622ViewSet

router = DefaultRouter()
router.register(
    "testconnectors135622", Testconnectors135622ViewSet, basename="testconnectors135622"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
