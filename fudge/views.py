# Create your views here.


from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'


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

def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})