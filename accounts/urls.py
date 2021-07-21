from django.urls import path
from . import views
from .forms import LoginForm
app_name = 'accounts'

urlpatterns = [
    path('register/',views.UserRegisterView.as_view(),name='register'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('profile/',views.profile,name='profile'),
]
