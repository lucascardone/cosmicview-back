from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=100)
    radius_km = models.FloatField()
    semi_major_axis_au = models.FloatField()
    eccentricity = models.FloatField()
    inclination_deg = models.FloatField()
    rotation_period_hours = models.FloatField()
    scaled_radius = models.FloatField()
    scaled_distance = models.FloatField()
    position_x = models.FloatField()
    position_y = models.FloatField()
    position_z = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Asteroid(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Nombre del asteroide
    semi_major_axis_au = models.FloatField()  # Radio promedio de la órbita en AU
    eccentricity = models.FloatField()  # Excentricidad de la órbita
    inclination_deg = models.FloatField()  # Inclinación en grados
    perihelion_distance = models.FloatField()  # Distancia del perihelio en AU
    aphelion_distance = models.FloatField()  # Distancia del afelio en AU
    mean_anomaly_deg = models.FloatField()  # Anomalía media
    argument_of_periapsis = models.FloatField()  # Argumento del perihelio
    longitude_of_ascending_node = models.FloatField()  # Longitud del nodo ascendente
    scaled_distance = models.FloatField()  # Distancia escalada al Sol
    is_potentially_hazardous = models.BooleanField(default=False)  # Si es potencialmente peligroso
    position_x = models.FloatField()  # Coordenada X de la posición actual
    position_y = models.FloatField()  # Coordenada Y de la posición actual
    position_z = models.FloatField()  # Coordenada Z de la posición actual
    last_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class Comet(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Nombre del cometa
    perihelion_distance = models.FloatField()  # Distancia del perihelio en AU
    semi_major_axis_au = models.FloatField()  # Radio promedio de la órbita en AU
    eccentricity = models.FloatField()  # Excentricidad de la órbita
    inclination_deg = models.FloatField()  # Inclinación en grados
    period_years = models.FloatField()  # Periodo orbital en años
    time_of_perihelion_passage = models.DateTimeField()  # Tiempo del paso por el perihelio
    scaled_distance = models.FloatField()  # Distancia escalada al Sol
    position_x = models.FloatField()  # Coordenada X de la posición actual
    position_y = models.FloatField()  # Coordenada Y de la posición actual
    position_z = models.FloatField()  # Coordenada Z de la posición actual
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

