from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Planet
from .serializers import PlanetSerializer
from .utils.orbital_propagator import calculate_orbit


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer


# Endpoint para obtener los puntos orbitales
@api_view(['GET'])
def get_orbital_data(request):
    planets = Planet.objects.all()

    data = {
        'planets': []
    }

    # Calcular los puntos orbitales de cada planeta
    for planet in planets:
        orbit_points = calculate_orbit(
            semi_major_axis=planet.semi_major_axis,
            eccentricity=planet.eccentricity,
            inclination=planet.inclination,
            mean_anomaly=0  # Esto es un valor inicial que puedes actualizar según necesites
        )
        data['planets'].append({
            'name': planet.name,
            'orbit': orbit_points
        })

    return Response(data)
