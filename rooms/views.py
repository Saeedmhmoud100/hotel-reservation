from django.shortcuts import render
from django.views.generic import ListView
from .models import Room
# Create your views here.

def home(request):
    return render(request,'room/home.html')

class HotelListView(ListView):
    template_name = 'room/hotel.html'
    model = Room


def hotel_single(request):
    return render(request,'room/hotel-single.html')

def tour(request):
    return render(request,'room/tour.html')

def tour_single(request):
    return render(request,'room/tour.html')

