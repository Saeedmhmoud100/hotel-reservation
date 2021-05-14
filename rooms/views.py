from django.shortcuts import render
from django.views.generic import ListView
from django_filters.views import FilterView

from .models import Room
# Create your views here.

def home(request):
    return render(request,'room/home.html')

class HotelListView(FilterView):
    template_name = 'room/hotel.html'
    model = Room
    paginate_by = 1
    filterset_fields = ['country', 'locality','data_from','data_to']
    
    def get_queryset(self):
        return super().get_queryset().filter(active=True)

    


def hotel_single(request,pk,slug):
    return render(request,'room/hotel-single.html')

def tour(request):
    return render(request,'room/tour.html')

def tour_single(request):
    return render(request,'room/tour.html')

