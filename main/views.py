from random import shuffle
from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models.query_utils import Q
from rooms.models import Room
from itertools import chain
from tours.models import Tour
from .models import Place
# Create your views here.

class HomeView(TemplateView):
    template_name = 'main/home.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['places'] = Place.objects.all()
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