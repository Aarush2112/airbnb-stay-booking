
from django.urls import path
from . import views

urlpatterns = [
    path(
        "history/",
        views.booking_history,
        name="booking_history"
    ),
    path(
        "cancel/<int:booking_id>/",
        views.cancel_booking,
        name="cancel_booking"
    ),
]
