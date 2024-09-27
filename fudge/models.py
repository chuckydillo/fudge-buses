from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
    

class BusInfoModel(models.Model):

    bus_company = models.CharField(max_length=200)
    bus_number = models.CharField(max_length=5)

class BusStops(models.Model):
    bus_info = models.ForeignKey(BusInfoModel, related_name="stops", on_delete=models.CASCADE)
    bus_stop = models.CharField(max_length=1000)
    bus_time = models.TimeField()