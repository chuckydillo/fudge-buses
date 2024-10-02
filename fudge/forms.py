from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import BusInfoModel, BusStopModel, BusReportModel

# User registration form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
# ------------------------------


class BusReportForm(forms.ModelForm):
    bus_info = forms.ModelChoiceField(queryset=BusInfoModel.objects.all(), empty_label="Select Bus Info")
    bus_stop = forms.ModelChoiceField(queryset=BusStopModel.objects.all(), empty_label="Select Bus Stop & Time") 
    class Meta:
        model = BusReportModel
        fields = ['bus_info', 'bus_stop', 'bus_report_date', 'bus_status', 'bus_delay_time']

        widgets = {
            'bus_report_date': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        bus_status = cleaned_data.get('bus_status')
        bus_delay_time = cleaned_data.get('bus_delay_time')

        if bus_status == 'late' and not bus_delay_time:
            self.add_error('bus_delay_time', 'Bus delay time is required if the bus is late.')

        return cleaned_data
# ------------------------------

class BusInfoForm(forms.ModelForm):

    class Meta:
        model = BusInfoModel
        fields = [
            'bus_company',
            'bus_number',
            ]

class BusStopForm(forms.ModelForm):
    class Meta:
        model = BusStopModel
        fields = [
            'bus_stop', 
            'bus_time',
            ]
        widgets = {
            'bus_time': forms.TimeInput(attrs={'type': 'time'}),
        }