from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlanetViewSet, get_orbital_data, get_position

router = DefaultRouter()
router.register('planets', PlanetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('positions/', get_position),  # Nuevo endpoint para órbitas
    path('orbits/', get_orbital_data),  # Nuevo endpoint para órbitas
]