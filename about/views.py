from django.shortcuts import render
from django.views.generic import ListView,View
from about.models import About, FAQ

# Create your views here.

class Aboutview(ListView):
    model = FAQ
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.last() 
        return context
    
class ContactView(View):
    def get(self,request, *args, **kwargs):
        return render(request,'about/contact.html')