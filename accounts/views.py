from django.shortcuts import redirect, render
from django.views.generic import View,DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model, login
from rooms.models import Room
from .forms import LoginForm, UserRegisterForm

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
        

class UserLoginView(LoginView):
    authentication_form = LoginForm
    form_class = LoginForm
    template_name = 'accounts/login.html'
    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        login(self.request, form.get_user())
        if not remember_me:
            self.request.session.set_expiry(0)
        return super(UserLoginView, self).form_valid(form)
class ProfileView(DetailView):
    model =  get_user_model()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.get_slug_field)
        context['object_list'] = Room.objects.filter(owner__slug=self.kwargs['slug'])
        return context

