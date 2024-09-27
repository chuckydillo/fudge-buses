# Create your views here.


from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login 
from .forms import CustomUserCreationForm # For user registratin
from django.contrib.auth.decorators import login_required
from .forms import BusInfoForm, BusStopForm
from .models import BusInfoModel, BusStopModel
#from .models import BusModel


# View for homepage
class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'

# View for user registration
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})

# View for profile
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

# View for Bus Report Form
def busreport_view(request):
    return render(request, 'bus/bus_report.html')

# Bus route creation form
@login_required
def bus_report(request):
    if request.method == 'POST':
        form = BusInfoForm(request.POST)
        if form.is_valid():
            bus_info = form.save()
            return redirect('bus_info_list')
    else:
        form = BusInfoForm()
    
    return render(request, 'bus/bus_report.html', {'form': form})


def bus_reports_view(request):
    # Query the database for all bus reports
    bus_reports = BusReport.objects.all()

    # Pass the bus reports to the template
    return render(request, 'bus_reports.html', {'bus_reports': bus_reports})


def bus_info_list(request):
    # Fetch all bus info entries from the database
    bus_infos = BusInfoModel.objects.all()

    # Pass the data to the template
    return render(request, 'bus/bus_info_list.html', {'bus_infos': bus_infos})
