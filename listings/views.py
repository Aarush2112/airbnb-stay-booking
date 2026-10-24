from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("""
        <h1>Airbnb Stay Booking System</h1>
        <p>Django project setup successful!</p>
        <p>Development is in progress.</p>
    """)