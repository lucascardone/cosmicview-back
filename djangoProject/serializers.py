from rest_framework import serializers
from .models import Planet, Asteroid, Comet

class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = [
            'name',
            'radius_km',
            'semi_major_axis_au',
            'eccentricity',
            'inclination_deg',
            'rotation_period_hours',
            'scaled_radius',
            'scaled_distance',
            'position_x',
            'position_y',
            'position_z',
            'last_updated'
        ]

class AsteroidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asteroid
        fields = [
            'name',
            'semi_major_axis_au',
            'eccentricity',
            'inclination_deg',
            'perihelion_distance',
            'aphelion_distance',
            'mean_anomaly_deg',
            'argument_of_periapsis',
            'longitude_of_ascending_node',
            'scaled_distance',
            'is_potentially_hazardous',
            'position_x',
            'position_y',
            'position_z',
            'last_updated'
        ]

class CometSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comet
        fields = [
            'name',
            'perihelion_distance',
            'semi_major_axis_au',
            'eccentricity',
            'inclination_deg',
            'period_years',
            'time_of_perihelion_passage',
            'scaled_distance',
            'position_x',
            'position_y',
            'position_z',
            'last_updated'
        ]
