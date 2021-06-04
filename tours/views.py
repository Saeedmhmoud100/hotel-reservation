from django.shortcuts import render

# Create your views here.


def tour(request):
    return render(request,'tours/tour.html')

def tour_single(request):
    return render(request,'tours/tour.html')