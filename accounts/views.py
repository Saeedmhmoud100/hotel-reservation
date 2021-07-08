from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import UserRegisterForm

# Create your views here.

class UserRegisterView(View):
    def get(self,request, *args, **kwargs):
        return render(request,'accounts/register.html',{'form':UserRegisterForm()})
    def post(self,request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
        else:
            print('yes')

            return render(request,'accounts/register.html',{'form':form})
    
def profile(request):
    return render(request,'profile.html')