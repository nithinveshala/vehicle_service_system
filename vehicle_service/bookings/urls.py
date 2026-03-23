from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Vehicle
    path('vehicles/', views.vehicle_list, name='vehicle_list'),
    path('vehicles/add/', views.vehicle_create, name='vehicle_create'),

    # Service
    path('services/', views.service_list, name='service_list'),
    path('services/add/', views.service_create, name='service_create'),

    # Booking
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/add/', views.booking_create, name='booking_create'),
]