#from django.urls import path
#from .views import HomePage, register
#from django.contrib.auth import views as auth_views

#urlpatterns = [
#    path('', HomePage.as_view(), name='home'),  # Home page
#    path('register/', register, name='register'),  # Register page
#    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Login page
#    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout page
#]


from . import views
from django.urls import path
from .views import HomePage, register, bus_report_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('register/', register, name='register'),  # Register page
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),  # Login page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout page
    path('profile/', views.profile_view, name='profile'),  # Profile page
    #path('bus_report/', views.busreport_view, name='bus_report'),  # Bus report form page
    path('bus_report/', bus_report_view, name='bus_report'),  # URL for the bus report form
    path('bus_add/', views.bus_add, name='bus_add'),  # URL for bus add form page
    path('bus-info/', views.bus_info_list, name='bus_info_list'),  # URL for viewing bus info list
]