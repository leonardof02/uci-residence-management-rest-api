from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from residence_management.models import Student, Building, Apartment, Room
from django.contrib.auth import authenticate
from .serializers import StudentSerializer, BuildingSerializer, ApartmentSerializer, RoomSerializer, StudentAssignmentSerializer, UserSerializer
from rest_framework.authtoken.models import Token

# Student Views
class StudentList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Building Views
class BuildingList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class BuildingDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

# Apartment Views
class ApartmentList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

class ApartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

# Room Views
class RoomList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class StudentAssignment(generics.GenericAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = StudentAssignmentSerializer

    def post(self, request):
        room_id = request.data.get("room_id")
        student_id = request.data.get("student_id")

        # Intenta obtener los objetos Room y Student
        try:
            room = Room.objects.get(id=room_id)
            student = Student.objects.get(student_id=student_id)
        except (Room.DoesNotExist, Student.DoesNotExist):
            return Response({"error": "Room or Student not found"}, status=404)

        # Verifica si el estudiante ya está en el cuarto
        if Student.objects.filter(room=room, student_id=student_id).exists():
            return Response({"error": "Ese estudiante ya se encuentra en este cuarto"}, status=400)

        # Verifica si el edificio está lleno
        if room.total_capacity <= 0:
            return Response({"error": "El edificio está lleno."}, status=400)

        # Asigna al estudiante al cuarto y guarda los cambios
        room.total_capacity -= 1
        student.room = room
        student.save()
        room.save()

        return Response({"message": f"Estudiante asignado exitosamente al apartamento: {room.apartment.building.number} {room.apartment.number}"}, status=200)

class RegisterUser(generics.CreateAPIView):
    serializer_class = UserSerializer

class LoginUser(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        
        user = authenticate(
            username=request.data['username'],
            password=request.data['password']
        )

        if not user:
            return Response({'error': 'Invalid credentials'}, status=401)

        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})