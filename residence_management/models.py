# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Building(models.Model):
    number = models.CharField(max_length=255, primary_key=True)
    faculty = models.CharField(max_length=255)
    year_of_students= models.IntegerField()
    sex_of_students= models.CharField(max_length=255)
    block = models.IntegerField()
    availability = models.BooleanField(max_length=255)

    instructor_in_charge = models.ForeignKey(User, on_delete=models.CASCADE)

class Apartment(models.Model):
    number = models.CharField(max_length=255)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

class StudentData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    ci = models.CharField(primary_key=True, max_length=255)
    username = models.CharField(max_length=255)

class Room(models.Model):
    total_capacity = models.IntegerField()
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)

class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    student_id = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    career = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    year = models.IntegerField()
    province = models.CharField(max_length=255)
    municipality = models.CharField(max_length=255)
    quarters_date = models.DateField(null=True)
    photo = models.URLField(null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    