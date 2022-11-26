from django.shortcuts import render

# Create your views here.
from .models import Reservation

def reserve_table(request):
    context = { 'saludo' : 'Hola desde las reservaciones...'}
    return render(request, 'Reservation/reservation.html', context)