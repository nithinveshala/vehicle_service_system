from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Vehicle, Service, Booking
from .forms import VehicleForm, ServiceForm, BookingForm


def home(request):
    context = {
        'vehicle_count': Vehicle.objects.count(),
        'service_count': Service.objects.count(),
        'booking_count': Booking.objects.count(),
        'today_booking_count': Booking.objects.filter(booking_date=timezone.localdate()).count(),
        'recent_bookings': Booking.objects.select_related('vehicle', 'service').order_by('-created_at')[:5],
    }
    return render(request, 'bookings/home.html', context)


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
