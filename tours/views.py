from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Tour
# Create your views here.


class TourListView(ListView):
    model = Tour

def tour_single(request):
    return render(request,'tours/tour.html')