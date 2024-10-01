from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
    

#class BusInfoModel(models.Model):
#
#    bus_company = models.CharField(max_length=200)
#    bus_number = models.CharField(max_length=5)

#class BusStopModel(models.Model):
#    bus_info = models.ForeignKey(BusInfoModel, related_name="stops", on_delete=models.CASCADE)
#    bus_stop = models.CharField(max_length=1000)
#    bus_time = models.TimeField()


class BusInfoModel(models.Model):
    bus_company = models.CharField(max_length=200)  # Name of the bus company
    bus_number = models.CharField(max_length=5)     # Number of the bus

    def __str__(self):
        return f"{self.bus_company} - {self.bus_number}"  # String representation for better readability

class BusStopModel(models.Model):
    bus_info = models.ForeignKey(
        BusInfoModel,
        related_name="stops",
        on_delete=models.CASCADE
    )
    bus_stop = models.CharField(max_length=1000)  # Name or description of the bus stop
    bus_time = models.TimeField()                   # Time the bus stops at this stop

    def __str__(self):
        return f"{self.bus_stop} at {self.bus_time}"  # String representation for better readability