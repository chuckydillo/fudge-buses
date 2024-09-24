from . import views
from django.urls import path
from .views import register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', 
        views.HomePage.as_view(), name='home'),
        path('register/', register, name='register'),
        path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
