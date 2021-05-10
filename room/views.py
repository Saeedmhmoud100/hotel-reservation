from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'room/home.html')


def tour(request):
    return render(request,'room/tour.html')

def tour_single(request):
    return render(request,'room/tour.html')

def hotel(request):
    return render(request,'room/hotel.html')

def hotel_single(request):
    return render(request,'room/hotel.html')