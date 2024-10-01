from rest_framework import serializers
from .models import Doctors, Direction

class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    directions = DirectionSerializer(many=True)

    class Meta:
        model = Doctors
        fields = '__all__'