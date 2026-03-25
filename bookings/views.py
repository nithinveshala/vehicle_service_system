from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehicle, Service, Booking
from .forms import VehicleForm, ServiceForm, BookingForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'bookings/home.html')


# ---------------- VEHICLE ----------------

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'bookings/vehicle_list.html', {'vehicles': vehicles})

def vehicle_create(request):
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('vehicle_list')
    return render(request, 'bookings/form.html', {'form': form, 'title': 'Add Vehicle'})


# ---------------- SERVICE ----------------

def service_list(request):
    services = Service.objects.all()
    return render(request, 'bookings/service_list.html', {'services': services})

def service_create(request):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('service_list')
    return render(request, 'bookings/form.html', {'form': form, 'title': 'Add Service'})


# ---------------- BOOKING ----------------

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

def booking_create(request):
    form = BookingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('booking_list')
    return render(request, 'bookings/form.html', {'form': form, 'title': 'Book Service'})