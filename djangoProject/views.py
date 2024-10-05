from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Planet
from .serializers import PlanetSerializer
from djangoProject.utils.planet.orbital_propagator import calculate_orbit, kepler_position, SCALE_FACTOR_SIZE
from datetime import datetime

class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer


@api_view(['GET'])
def get_position(request):
    # Obtener la fecha y hora de los parámetros de consulta (formato: YYYY-MM-DD HH:MM)
    date_param = request.query_params.get('date', None)

    if date_param:
        try:
            # Intentamos parsear la fecha y hora en formato 'YYYY-MM-DD HH:MM'
            date = datetime.strptime(date_param, '%Y-%m-%d %H:%M')
        except ValueError:
            return Response({
                "error": "Formato de fecha y hora inválido. Utiliza el formato 'YYYY-MM-DD HH:MM'."
            }, status=400)
    else:
        # Si no se proporciona la fecha y hora, se usa la fecha y hora actuales
        date = datetime.now()

    planets = Planet.objects.all()

    data = {
        'planets': []
    }

    # Calcular los puntos orbitales de cada planeta
    for planet in planets:
        position_points = kepler_position(planet, date)  # Pasar la fecha y hora a kepler_position
        orbit_points = calculate_orbit(planet)
        data['planets'].append({
            'name': planet.name,
            'radius': planet.radius_km / SCALE_FACTOR_SIZE,
            'position': position_points,
            'orbit': orbit_points
        })

    return Response(data)
