from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    HomePage, register, user_bus_report_view, edit_bus_report_view,
    delete_bus_report_view, user_bus_report_history_view, AboutView,
    edit_bus_info_view, delete_bus_info_view
)

urlpatterns = [
    # Account related URLs
    path('', HomePage.as_view(), name='home'),  # Home page
    path('register/', register, name='register'),  # Registration page
    # Login page
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='accounts/login.html'),
        name='login'
    ),
    # Logout page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),  # Profile page
    # Account creation confirmation page
    path(
        'account_success/',
        views.account_success,
        name='account_success'
    ),

    # User URLs
    # User bus report page
    path(
        'user-bus-report/', user_bus_report_view, name='user_bus_report'
    ),
    # Bus report history page
    path(
        'user-bus-report-history/',
        user_bus_report_history_view,
        name='user_bus_report_history'
    ),
    # Edit bus report page
    path(
        'edit-bus-report/<int:report_id>/',
        edit_bus_report_view,
        name='edit_bus_report'
    ),
    # Delete bus report page
    path(
        'delete-bus-report/<int:report_id>/',
        delete_bus_report_view,
        name='delete_bus_report'
    ),

    # Admin URLs
    path('bus-add/', views.bus_add, name='bus_add'),  # Add new bus report page
    path('bus-info/', views.bus_info_list, name='bus_info_list'),  # Bus info list page
    # Edit bus info page
    path(
        'edit-bus-info/<int:bus_id>/',
        edit_bus_info_view,
        name='edit_bus_info'
    ),
    # Delete bus info page
    path(
        'delete-bus-info/<int:bus_id>/',
        delete_bus_info_view,
        name='delete_bus_info'
    ),

    # Misc URLs
    path('about/', AboutView.as_view(), name='about'),  # About page
]