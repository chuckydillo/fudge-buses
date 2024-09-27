from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
    

class BusInfoModel(models.Model):

    bus_company = models.CharField(max_length=200)
    bus_number = models.CharField(max_length=5)
    bus_stop = models.CharField(max_length=300)
    bus_time = models.TimeField()