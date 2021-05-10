from django.urls import path
from . import views

app_name = 'room'

urlpatterns = [
    path('', views.home,name='home'),
    path('tour', views.tour,name='tour'),
    path('tour_single', views.tour_single,name='tour_single'),
    path('hotel', views.hotel,name='hotel'),
    path('hotel_single', views.hotel_single,name='hotel_single'),

]
