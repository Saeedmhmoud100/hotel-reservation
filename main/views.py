from random import shuffle
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Place
# Create your views here.

class HomeView(TemplateView):
    template_name = 'main/home.html'
    
def places_search(request):
    context={
        'post_list':[1,2,3,4,5,6,7,8,9]
    }
    return render(request,'main/search.html',context)