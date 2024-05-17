from rest_framework import generics
from residence_management.serializers import UserSerializer, ApartmentSerializer
from residence_management.models import Apartment
from django.contrib.auth.models import User

# Create your views here
class ApartmentCreateView(generics.CreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

class ApartmentListView(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

# Detalle de un apartamento
class ApartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer