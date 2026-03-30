from django.contrib import admin
from django.urls import path, include
from bookings.views import CustomerLoginView, CustomerLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookings.urls')),

    path('login/', CustomerLoginView.as_view(), name='login'),
    path('logout/', CustomerLogoutView.as_view(), name='logout'),
]
