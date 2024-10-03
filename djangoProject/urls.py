from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlanetViewSet

router = DefaultRouter()
router.register('planets', PlanetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
