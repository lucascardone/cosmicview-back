from django.http import JsonResponse
from djangoProject.models import Planet, Asteroid, Comet
from math import cos, sin, radians
import numpy as np
from datetime import datetime, timedelta
from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, get_body_barycentric_posvel

SCALE_FACTOR_SIZE = 1000
SCALE_FACTOR_DISTANCE = 100

def calculate_planet_position(planet_name, date):
    # Convertimos la fecha a un objeto de tiempo
    time = Time(date)
    # Usamos las efemérides para obtener la posición del planeta
    with solar_system_ephemeris.set('builtin'):
        pos, vel = get_body_barycentric_posvel(planet_name, time)

    scaled_pos = (pos.xyz.value[0] * SCALE_FACTOR_DISTANCE,
                    pos.xyz.value[1] * SCALE_FACTOR_DISTANCE,
                    pos.xyz.value[2] * SCALE_FACTOR_DISTANCE)

    return scaled_pos  # Devuelve las coordenadas x, y, z en AU


def calculate_orbit(planet_name, start_date, total_days):
    # Convertir la fecha de inicio a un objeto de tiempo
    start_time = Time(start_date)

    orbit_points = []  # Lista para almacenar los puntos de la órbita

    # Calcular la posición del planeta en 64 puntos distribuidos a lo largo de total_days
    interval = total_days / 240 # Intervalo de días entre cada punto
    for i in range(240):
        # Calcular la fecha para el punto actual
        current_time = start_time + timedelta(days=i * interval)

        # Usar las efemérides para obtener la posición del planeta
        with solar_system_ephemeris.set('builtin'):
            pos, _ = get_body_barycentric_posvel(planet_name, current_time)

        # Agregar la posición (x, y, z) a la lista
        scaled_pos = (pos.xyz.value[0] * SCALE_FACTOR_DISTANCE,
                      pos.xyz.value[1] * SCALE_FACTOR_DISTANCE,
                      pos.xyz.value[2] * SCALE_FACTOR_DISTANCE)

        orbit_points.append(scaled_pos)

    return np.array(orbit_points)  # Devuelve los puntos de la órbita en forma de array