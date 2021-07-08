from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm
app_name = 'accounts'

urlpatterns = [
    path('register/',views.UserRegisterView.as_view(),name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html',authentication_form=LoginForm),name='login'),
    path('profile/',views.profile,name='profile'),
]
