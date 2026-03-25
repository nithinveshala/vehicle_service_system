from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Booking, Service, Vehicle


class BookingViewsTestCase(TestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(
            owner_name='Nithin',
            email='nithin@example.com',
            vehicle_number='TS09AB1234',
            vehicle_type='Car',
        )
        self.service = Service.objects.create(
            service_name='Oil Change',
            price='1499.00',
            description='Engine oil replacement',
        )

    def test_home_page_loads(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Vehicle Service Booking System')

    def test_vehicle_list_shows_saved_vehicle(self):
        response = self.client.get(reverse('vehicle_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.vehicle.vehicle_number)

    def test_booking_create_saves_booking(self):
        response = self.client.post(
            reverse('booking_create'),
            {
                'vehicle': self.vehicle.id,
                'service': self.service.id,
                'booking_date': date.today().isoformat(),
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Booking.objects.count(), 1)
