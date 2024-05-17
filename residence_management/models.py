from django.db import models

# Create your models here.
class Apartment(models.Model):
    number = models.CharField(max_length=255)
    num_rooms = models.IntegerField()