from rest_framework import serializers
from .models import Planet, Asteroid, Comet

class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'

class AsteroidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asteroid
        fields = '__all__'

class CometSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comet
        fields = '__all__'
