from rest_framework import generics
from rest_framework.response import Response
from residence_management.models import Student, Building, Apartment, Room
from .serializers import StudentSerializer, BuildingSerializer, ApartmentSerializer, RoomSerializer, StudentAssignmentSerializer

# Student Views
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Building Views
class BuildingList(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class BuildingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

# Apartment Views
class ApartmentList(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

class ApartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

# Room Views
class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class StudentAssignment(generics.GenericAPIView):
    serializer_class = StudentAssignmentSerializer

    def post(self, request):

        room_id = request.data.get("room_id")
        student_id = request.data.get("student_id")

        room =  Room.objects.get(id=room_id)
        student = Student.objects.get(student_id=student_id)

        students_in_room = Student.objects.filter(room=room)
        is_this_student_in_that_room = students_in_room.filter(student_id=student_id).exists()

        if(is_this_student_in_that_room):
            return Response({"error": "Ese estudiante ya se encuentra en este cuarto"}, status=400)

        if room.total_capacity <= 0:
            return Response({"error": "El edificio está lleno."}, status=400)
        
        room.total_capacity -= 1
        student.room = room
        student.save()
        room.save()
        return Response({"message": f"Estudiante asignado exitosamente al apartamento: {room.apartment.building.number} {room.apartment.number}"}, status=200)