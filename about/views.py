from django.shortcuts import render
from django.views.generic import ListView
from about.models import FAQ

# Create your views here.

class Aboutview(ListView):
    model = FAQ
    
def contact(request):
    return render(request,'about/contact.html')