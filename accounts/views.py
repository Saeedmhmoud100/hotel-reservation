from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.views.generic import View,DetailView,UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model, login
from rooms.models import Room
from .forms import LoginForm, UserRegisterForm, UserUpdateForm

# Create your views here.

class UserRegisterView(View):
    def get(self,request, *args, **kwargs):
        return render(request,'accounts/user_form.html',{'form':UserRegisterForm()})
    def post(self,request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        else:
            print('yes')

            return render(request,'accounts/user_form.html',{'form':form})
        

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
    def get_success_url(self):
        return self.request.user.get_absolute_url()
    
class ProfileView(DetailView):
    model =  get_user_model()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.get_slug_field)
        context['object_list'] = Room.objects.filter(owner__slug=self.kwargs['slug'])
        return context

def profile_option(request,slug):
    obj = None
    title = None
    if slug == 'rooms' : obj = request.user.room_set.all()
    if slug == 'tours' : obj = request.user.tour_set.all()
    if slug == 'posts' : obj = request.user.post_set.all();title='posts'
    context={
        'object_list':obj,'title':title,
    }
    t = render_to_string('accounts/profile_option.html',context)
    data = {
        'data':t,
        'title':'Your '+slug.title(),
        'checked':False
    }
    return JsonResponse(data)

def toggle_profile_option(request,slug):
    checked = request.POST.get('show_moving_carts',False)
    get_user_model().objects.filter(slug=slug).update(toggle_cart_option= True if checked=='on' else False )
    return redirect('accounts:profile',slug)
class ProfileUpdateView(UpdateView):
    model=get_user_model()
    form_class=UserUpdateForm
    def get_success_url(self):
        return self.get_object().get_absolute_url()
    
