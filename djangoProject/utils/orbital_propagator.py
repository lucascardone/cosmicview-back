from django.http import JsonResponse
from ..models import Planet, Asteroid, Comet
from math import cos, sin, radians
import numpy as np
from datetime import datetime

def kepler_position(body, date=None):
    # Parámetros orbitales
    a = body.semi_major_axis * 149597870.7 # Eje semi-mayor (distancia media al Sol, representa el tamaño de la órbita)
    e = body.eccentricity # Excentricidad orbital (cuán elíptica es la órbita)
    i = np.radians(body.inclination) # Inclinación orbital convertida a radianes (La inclinación de la órbita respecto al plano de referencia)
    Ω = np.radians(body.longitude_ascending_node) # Longitud del nodo ascendente (convertida a radianes)
    ω = np.radians(body.longitude_perihelion) # Longitud del perihelio (convertida a radianes)
    M_0 = np.radians(body.mean_longitude) # Longitud media (convertida a radianes)
    T = body.orbital_period  # Periodo orbital en días

    # Calcular el tiempo actual o un tiempo específico
    if date is None:
        date = datetime.now()  # Usamos la fecha actual si no se pasa ninguna fecha

    # Tiempo de la época (t_0) --> la epoch de J2000
    epoch_time = datetime(2000, 1, 1, 12, 0, 0)
    delta_t = (date - epoch_time).total_seconds() / (60 * 60 * 24)  # Diferencia en días julianos


    # Ajustes por siglo
    #centuries = (date.year - 2000) / 100
    #i += centuries * body.inclination_rate_per_century  # Ajustar inclinación
    #Ω += centuries * body.longitude_ascending_node_rate_per_century  # Ajustar nodo ascendente
    #ω += centuries * body.longitude_perihelion_rate_per_century  # Ajustar perihelio

    # Movimiento medio angular (n)
    n = 2 * np.pi / T  # n = 2π / T

    # Anomalía media en el tiempo t
    M = M_0 + n * delta_t  # M(t) = M_0 + n(t - t_0)

    # Resolver la ecuación de Kepler para obtener E, ν, r (igual que antes)
    E = M  # Estimación inicial
    for _ in range(100):
        E = E - (E - e * np.sin(E) - M) / (1 - e * np.cos(E))

    ν = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2), np.sqrt(1 - e) * np.cos(E / 2))
    r = a * (1 - e * np.cos(E))

    # Coordenadas en el plano orbital
    x_orb = r * np.cos(ν)
    y_orb = r * np.sin(ν)

    # Convertir a coordenadas 3D en el espacio
    x = (np.cos(Ω) * np.cos(ω + ν) - np.sin(Ω) * np.sin(ω + ν) * np.cos(i)) * r
    y = (np.sin(Ω) * np.cos(ω + ν) + np.cos(Ω) * np.sin(ω + ν) * np.cos(i)) * r
    z = (np.sin(ω + ν) * np.sin(i)) * r

    return x, y, z


def calculate_orbit(body, num_points=64):
    # Parámetros orbitales del planeta
    a = body.semi_major_axis * 149597870.7  # Eje semi-mayor
    e = body.eccentricity  # Excentricidad
    i = np.radians(body.inclination)  # Inclinación en radianes
    Ω = np.radians(body.longitude_ascending_node)  # Longitud del nodo ascendente en radianes
    ω = np.radians(body.longitude_perihelion)  # Argumento del perihelio en radianes

    orbit_points = []  # Lista para almacenar los puntos de la órbita

    # Recorremos diferentes ángulos para la anomalía verdadera ν (de 0° a 360°)
    for angle in np.linspace(0, 2 * np.pi, num_points):
        # Calcular r y ν para el ángulo actual
        r = a * (1 - e ** 2) / (1 + e * cos(angle))  # Distancia radial usando la ley de órbitas de Kepler
        ν = angle  # Anomalía verdadera

        # Coordenadas en el plano orbital
        x_orb = r * cos(ν)
        y_orb = r * sin(ν)

        # Convertir a coordenadas 3D usando las rotaciones keplerianas
        x = (cos(Ω) * cos(ω + ν) - sin(Ω) * sin(ω + ν) * cos(i)) * r
        y = (sin(Ω) * cos(ω + ν) + cos(Ω) * sin(ω + ν) * cos(i)) * r
        z = (sin(ω + ν) * sin(i)) * r

        # Almacenar el punto en 3D
        orbit_points.append({'x': x, 'y': y, 'z': z})

    return orbit_points