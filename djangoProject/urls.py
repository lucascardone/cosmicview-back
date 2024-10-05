from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlanetViewSet, get_position

router = DefaultRouter()
router.register('planets', PlanetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('all/', get_position),  # Nuevo endpoint para órbitas
]