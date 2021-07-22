from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
app_name = 'accounts'

urlpatterns = [
    path('register/',views.UserRegisterView.as_view(),name='register'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
    path('profile/<slug:slug>/',views.ProfileView.as_view(),name='profile'),
    path('profile/<slug:slug>/update/',views.ProfileUpdateView.as_view(),name='profile-update'),
]
