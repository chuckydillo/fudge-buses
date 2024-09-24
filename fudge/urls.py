from django.urls import path
from .views import HomePage, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomePage.as_view(), name='home'),  # Home page
    path('register/', register, name='register'),  # Register page
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Login page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout page
]