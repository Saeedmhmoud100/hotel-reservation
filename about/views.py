from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,View
from django.contrib import messages
from about.models import About, FAQ
from main.models import Info
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

class Aboutview(ListView):
    model = FAQ
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.last() 
        return context
    
class ContactView(View):
    def get(self,request, *args, **kwargs):
        return render(request,'about/contact.html',{'info':Info.objects.last()})
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        subject = request.POST['subject']
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            subject,
            f'message from {name} \n email : {email} \n Message : {message}',
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        messages.success(request,'sended email successfully!!')
        return render(request,'about/contact.html',{'info':Info.objects.last()})