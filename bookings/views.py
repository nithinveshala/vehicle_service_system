from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Vehicle, Service, Booking
from .forms import VehicleForm, ServiceForm, BookingForm, CustomerLoginForm, CustomerRegisterForm
from django.contrib.auth.decorators import login_required


class CustomerLoginView(LoginView):
    template_name = 'bookings/login.html'
    authentication_form = CustomerLoginForm
    redirect_authenticated_user = True


class CustomerLogoutView(LogoutView):
    http_method_names = ['post']


def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = CustomerRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')

    return render(request, 'bookings/register.html', {'form': form})


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

@login_required
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

@login_required
def service_create(request):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('service_list')
    return render(request, 'bookings/form.html', {'form': form, 'title': 'Add Service'})


# ---------------- BOOKING ----------------

@login_required
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

@login_required
def booking_create(request):
    form = BookingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('booking_list')
    return render(request, 'bookings/form.html', {'form': form, 'title': 'Book Service'})
