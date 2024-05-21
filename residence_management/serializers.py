from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student, Building, Apartment, Room

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student 
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):

    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = "__all__"

class ApartmentSerializer(serializers.ModelSerializer):

    rooms = RoomSerializer(many=True, read_only=True )

    class Meta:
        model = Apartment 
        fields = "__all__"

class BuildingSerializer(serializers.ModelSerializer):

    apartments = ApartmentSerializer(many=True, read_only=True)

    class Meta:
        model = Building 
        fields = "__all__"

class StudentAssignmentSerializer(serializers.Serializer):
    room_id = serializers.IntegerField()
    student_id = serializers.CharField()