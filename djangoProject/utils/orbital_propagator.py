from django.http import JsonResponse
from ..models import Planet, Asteroid, Comet
from math import cos, sin, radians
import numpy as np

def kepler_position(body):
    a = body.semi_major_axis
    e = body.eccentricity
    i = np.radians(body.inclination)
    Ω = np.radians(body.longitude_ascending_node)
    ω = np.radians(body.longitude_perihelion)
    M = np.radians(body.mean_longitude)

    # Resolver la ecuación de Kepler (como antes) para obtener E, ν, r
    E = M  # Estimación inicial
    for _ in range(100):
        E = E - (E - e * np.sin(E) - M) / (1 - e * np.cos(E))

    ν = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2), np.sqrt(1 - e) * np.cos(E / 2))
    r = a * (1 - e * np.cos(E))

    # Coordenadas en el plano orbital
    x_orb = r * np.cos(ν)
    y_orb = r * np.sin(ν)

    # Convertir a 3D
    x = (np.cos(Ω) * np.cos(ω + ν) - np.sin(Ω) * np.sin(ω + ν) * np.cos(i)) * r
    y = (np.sin(Ω) * np.cos(ω + ν) + np.cos(Ω) * np.sin(ω + ν) * np.cos(i)) * r
    z = (np.sin(ω + ν) * np.sin(i)) * r

    return x, y, z


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