
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import Booking


@login_required
def booking_history(request):
    today = timezone.localdate()

    # Fetch only the logged-in user's bookings
    bookings = Booking.objects.filter(
        user=request.user
    ).order_by("-created_at")

    # Separate bookings into categories
    upcoming = bookings.filter(
        status__in=[
            Booking.Status.PENDING,
            Booking.Status.CONFIRMED
        ],
        check_out__gte=today
    )

    completed = bookings.filter(
        status=Booking.Status.COMPLETED
    ) | bookings.filter(
        check_out__lt=today
    ).exclude(status=Booking.Status.CANCELLED)

    cancelled = bookings.filter(
        status=Booking.Status.CANCELLED
    )

    context = {
        "upcoming_bookings": upcoming,
        "completed_bookings": completed.distinct(),
        "cancelled_bookings": cancelled,
    }

    return render(
        request,
        "bookings/booking_history.html",
        context
    )


@login_required
@require_POST
def cancel_booking(request, booking_id):
    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user
    )

    today = timezone.localdate()

    if booking.status not in [
        Booking.Status.PENDING,
        Booking.Status.CONFIRMED
    ]:
        messages.error(
            request,
            "This booking cannot be cancelled."
        )

    elif booking.check_in <= today:
        messages.error(
            request,
            "Bookings cannot be cancelled on or after check-in."
        )

    else:
        booking.status = Booking.Status.CANCELLED
        booking.save(update_fields=["status"])

        messages.success(
            request,
            "Your booking has been cancelled successfully."
        )

    return redirect("booking_history")
