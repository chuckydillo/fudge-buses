# Create your views here.


from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login 
from .forms import CustomUserCreationForm # For user registratin
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from .forms import BusInfoForm, BusStopForm, BusReportForm
from .models import BusInfoModel, BusStopModel, BusReportModel
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

# Fetch all bus info entries from the database
def bus_info_list(request):
    bus_infos = BusInfoModel.objects.prefetch_related('stops').all()

    return render(request, 'bus/bus_info_list.html', {'bus_infos': bus_infos})

# Form to add bus routes
def bus_add(request):
    BusStopModelFormSet = modelformset_factory(BusStopModel, form=BusStopForm, extra=1)

    if request.method == 'POST':
        bus_form = BusInfoForm(request.POST)
        formset = BusStopModelFormSet(request.POST)

        if bus_form.is_valid() and formset.is_valid():
            bus_info = bus_form.save()
            for form in formset:
                if form.cleaned_data:
                    bus_stop_time = form.save(commit=False)
                    bus_stop_time.bus_info = bus_info
                    bus_stop_time.save()

            return redirect('bus_info_list')
    else:
        bus_form = BusInfoForm()
        formset = BusStopModelFormSet(queryset=BusStopModel.objects.none())

    return render(request, 'bus/bus_add.html', {'bus_form': bus_form, 'formset': formset})

# Form to report buses

@login_required
def bus_report_view(request):
    if request.method == 'POST':
        form = BusReportForm(request.POST)
        if form.is_valid():
            form.save()  # Save the bus report if valid
            return redirect('home')  # Redirect to a success page or home page
    else:
        form = BusReportForm()  # Create an empty form for GET request

   
    return render(request, 'bus/bus_report.html', {'form': form})