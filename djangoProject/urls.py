from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlanetViewSet, get_orbital_data

router = DefaultRouter()
router.register('planets', PlanetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('planets/orbits/', get_orbital_data),  # Nuevo endpoint para órbitas
]