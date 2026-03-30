from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Booking, Service, Vehicle


class BookingViewsTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='customer1',
            password='StrongPass123!',
        )
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
        response = self.client.get(reverse('home'), secure=True, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Vehicle Service Dashboard')

    def test_vehicle_list_shows_saved_vehicle(self):
        response = self.client.get(reverse('vehicle_list'), secure=True, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.vehicle.vehicle_number)

    def test_booking_list_requires_login(self):
        response = self.client.get(reverse('booking_list'), secure=True)

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response['Location'])

    def test_customer_can_log_in(self):
        response = self.client.post(
            reverse('login'),
            {
                'username': 'customer1',
                'password': 'StrongPass123!',
            },
            secure=True,
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertContains(response, 'customer1')

    def test_customer_can_log_out(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('logout'), secure=True, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertContains(response, 'Customer Login')

    def test_booking_create_saves_booking(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('booking_create'),
            {
                'vehicle': self.vehicle.id,
                'service': self.service.id,
                'booking_date': date.today().isoformat(),
            },
            secure=True,
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Booking.objects.count(), 1)
