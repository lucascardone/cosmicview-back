from django.http import JsonResponse
from ..models import Planet, Asteroid, Comet
from math import cos, sin, radians

def calculate_orbit(semi_major_axis, eccentricity, inclination):
    # Aquí iría la fórmula para calcular la órbita, en este caso usando datos simulados
    points = []
    for angle in range(0, 360, 10):
        angle_rad = radians(angle)
        r = semi_major_axis * (1 - eccentricity**2) / (1 + eccentricity * cos(angle_rad))
        x = r * cos(angle_rad)
        y = r * sin(angle_rad)
        z = r * sin(radians(inclination))  # Considerar inclinación en el plano Z
        points.append({'x': x, 'y': y, 'z': z})
    return points