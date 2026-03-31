from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
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


class CustomerRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Customer username',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Choose a username',
                'autocomplete': 'username',
            }
        ),
    )
    email = forms.EmailField(
        label='Email address',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Enter your email',
                'autocomplete': 'email',
            }
        ),
    )
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Create a password',
                'autocomplete': 'new-password',
            }
        ),
    )
    password2 = forms.CharField(
        label='Confirm password',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm your password',
                'autocomplete': 'new-password',
            }
        ),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

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
