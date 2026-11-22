
from datetime import timedelta

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

from .models import Booking


User = get_user_model()


class BookingHistoryTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="tanvi",
            password="testpassword123"
        )

        self.other_user = User.objects.create_user(
            username="otheruser",
            password="testpassword123"
        )

        self.client.login(
            username="tanvi",
            password="testpassword123"
        )

    def create_booking(self, user, check_in, check_out):
        return Booking.objects.create(
            user=user,
            check_in=check_in,
            check_out=check_out,
            guests=2,
            status=Booking.Status.CONFIRMED
        )

    def test_user_sees_only_own_bookings(self):
        today = timezone.localdate()

        own_booking = self.create_booking(
            self.user,
            today + timedelta(days=5),
            today + timedelta(days=7)
        )

        other_booking = self.create_booking(
            self.other_user,
            today + timedelta(days=8),
            today + timedelta(days=10)
        )

        response = self.client.get(reverse("booking_history"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f"Booking #{own_booking.id}")
        self.assertNotContains(response, f"Booking #{other_booking.id}")

    def test_user_can_cancel_own_booking(self):
        today = timezone.localdate()

        booking = self.create_booking(
            self.user,
            today + timedelta(days=5),
            today + timedelta(days=7)
        )

        response = self.client.post(
            reverse("cancel_booking", args=[booking.id])
        )

        booking.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            booking.status,
            Booking.Status.CANCELLED
        )

    def test_user_cannot_cancel_another_users_booking(self):
        today = timezone.localdate()

        booking = self.create_booking(
            self.other_user,
            today + timedelta(days=5),
            today + timedelta(days=7)
        )

        response = self.client.post(
            reverse("cancel_booking", args=[booking.id])
        )

        booking.refresh_from_db()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            booking.status,
            Booking.Status.CONFIRMED
        )

    def test_booking_cannot_be_cancelled_on_or_after_check_in(self):
        today = timezone.localdate()

        for days in [0, -1]:
            with self.subTest(days=days):
                booking = self.create_booking(
                    self.user,
                    today + timedelta(days=days),
                    today + timedelta(days=days + 2)
                )

                self.client.post(
                    reverse("cancel_booking", args=[booking.id])
                )

                booking.refresh_from_db()

                self.assertEqual(
                    booking.status,
                    Booking.Status.CONFIRMED
                )

    
    def test_booking_history_requires_login(self):
        self.client.logout()

        response = self.client.get(
            reverse("booking_history")
        )

        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)

    def test_get_request_cannot_cancel_booking(self):
        today = timezone.localdate()

        booking = self.create_booking(
            self.user,
            today + timedelta(days=5),
            today + timedelta(days=7)
        )

        response = self.client.get(
            reverse("cancel_booking", args=[booking.id])
        )

        booking.refresh_from_db()

        self.assertEqual(response.status_code, 405)
        self.assertEqual(
            booking.status,
            Booking.Status.CONFIRMED
        )

