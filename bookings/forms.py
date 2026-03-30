from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Vehicle, Service, Booking


class CustomerLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Customer username',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your username',
                'autocomplete': 'username',
            }
        ),
    )
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter your password',
                'autocomplete': 'current-password',
            }
        ),
    )

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
