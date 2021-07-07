from django.urls import path
from . import views


app_name = 'about'

urlpatterns = [
    path('', views.Aboutview.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
