from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

# Create your models here.
    


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

class BusReportModel(models.Model):
    bus_info = models.ForeignKey(BusInfoModel, on_delete=models.CASCADE, null=True, blank=True)
    bus_report_date = models.DateField(null=True, blank=True) # Date of delay

    BUS_STATUS_CHOICES  = [
        ('on_time', 'On Time'),
        ('late', 'Late'),
        ('cancelled', 'Cancelled'),
    ]
    bus_status = models.CharField(max_length=15, choices=BUS_STATUS_CHOICES)

    BUS_DELAY_CHOICES  = [
    ('0-5', 'Less than 5 minutes'),
    ('5-10', 'Between 5 and 10 minutes'),
    ('10-20', 'between 10 and 20 minutes'),
    ('20+', 'More than 20 minutes'),
    ]
    bus_delay_time = models.CharField(max_length=30, choices=BUS_DELAY_CHOICES, blank=True)  # Optional if not late

    def __str__(self):
        return f"Bus Report: {self.bus_status}"
