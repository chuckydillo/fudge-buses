from django.shortcuts import render, redirect
# Create your views here.

from django.views.generic import TemplateView
from django.contrib.auth import login
from .forms import CustomUserCreationForm

class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            login(request, user)  # Log in the user after registration
            return redirect('index')  # Redirect to homepage or a success page
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})