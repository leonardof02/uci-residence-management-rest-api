from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student, Building, Apartment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student 
        fields = "__all__"

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building 
        fields = "__all__"

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment 
        fields = "__all__"