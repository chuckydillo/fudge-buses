from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import BusInfoModel, BusStopsModel

# User registration form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


#class BusForm(forms.Form):
#    bus_company = forms.ChoiceField(
#        choices=[('delay', 'Delay'), ('incident', 'Incident'), ('maintenance', 'Maintenance')],
#        label='Bus Company'
#    )
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
        model = BusStops
        fields = [
            'bus_stop', 
            'bus_time',
            ]
        widgets = {
            'bus_time': forms.TimeInput(attrs={'type': 'time'}),
        }