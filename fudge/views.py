#from django.shortcuts import render, redirect
# Create your views here.

#from django.views.generic import TemplateView
#from django.contrib.auth import login
#from .forms import CustomUserCreationForm

from django.shortcuts import render
from django.views.generic import TemplateView

class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'


#def register(request):
#    if request.method == 'POST':
#        form = CustomUserCreationForm(request.POST)
#        if form.is_valid():
#            user = form.save()
#            login(request, user)
#            return redirect('index')
#    else:
#        form = CustomUserCreationForm()
#
#    return render(request, 'registration/register.html', {'form': form})
