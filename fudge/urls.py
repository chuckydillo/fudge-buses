from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomePage, register, user_bus_report_view, edit_bus_report_view, delete_bus_report_view, user_bus_report_history_view, AboutView, edit_bus_info_view, delete_bus_info_view


urlpatterns = [
    # Account related urls
    path('', views.HomePage.as_view(), name='home'),  # Home page
    path('register/', views.register, name='register'),  # Registration page
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),  # Login page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout page
    path('profile/', views.profile_view, name='profile'),  # Profile page
    path('account_success/', views.account_success, name='account_success'), # Account creation confirm page

    # User urls
    path('user-bus-report/', views.user_bus_report_view, name='user_bus_report'),  # User bus report page
    path('user-bus-report-history/', views.user_bus_report_history_view, name='user_bus_report_history'),  # Bus report history page
    path('edit-bus-report/<int:report_id>/', views.edit_bus_report_view, name='edit_bus_report'),  # Edit bus report page
    path('delete-bus-report/<int:report_id>/', views.delete_bus_report_view, name='delete_bus_report'),  # Delete bus report page
    

    # Admin urls
    path('bus-add/', views.bus_add, name='bus_add'),  # Add new bus report page
    path('bus-info/', views.bus_info_list, name='bus_info_list'),  # Bus information list page
    path('edit-bus-info/<int:bus_id>/', edit_bus_info_view, name='edit_bus_info'),  # Edit bus info page
    path('delete-bus-info/<int:bus_id>/', delete_bus_info_view, name='delete_bus_info'),  # Delete bus info page
    
    # Misc urls
    path('about/', AboutView.as_view(), name='about'),
]
