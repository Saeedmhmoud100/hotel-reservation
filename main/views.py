from random import shuffle
from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models.query_utils import Q
from django.db.models.aggregates import Count
from rooms.models import Room
from itertools import chain
from tours.models import Tour
from .models import Home_Cart, Place,Category
# Create your views here.

class HomeView(TemplateView):
    template_name = 'main/home.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['places'] = Place.objects.all().annotate(rooms=Count('room'),tours=Count('tour'))
        context['Categorys']=Category.objects.all()
        context['Home_Carts']=Home_Cart.objects.all()[:4]
        context['top_tours']=Tour.objects.all().order_by('tour_Reservation')[:5]
        return context
    
def places_search(request):
    name = request.GET.get('name','')
    place = request.GET.get('place','')
    rooms=Room.objects.filter(
        Q(city__name__icontains=place) &
        Q(title__icontains=name) |
        Q(descriptions__icontains=name)
    )
    tours=Tour.objects.filter(
        Q(city__name__icontains=place) &
        Q(title__icontains=name) |
        Q(descriptions__icontains=name)
    )
    res = list(chain(rooms,tours))
    shuffle(res)
    return render(request,'main/search.html',{'response':res})

def category_filter(request,category):
    rooms=Room.objects.filter(category__name=category)
    tours=Tour.objects.filter(category__name=category)
    res = list(chain(rooms,tours))
    shuffle(res)
    return render(request,'main/search.html',{'response':res})

def place_filter(request,place):
    rooms=Room.objects.filter(city__name=place)
    tours=Tour.objects.filter(city__name=place)
    res = list(chain(rooms,tours))
    shuffle(res)
    return render(request,'main/search.html',{'response':res})