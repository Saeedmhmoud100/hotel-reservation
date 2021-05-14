from django.urls import path
from . import views


app_name = 'rooms'

urlpatterns = [
    path('', views.home,name='home'),
    path('hotel', views.HotelListView.as_view(),name='hotel'),
    path('hotel_single', views.hotel_single,name='hotel_single'),
    path('tour', views.tour,name='tour'),
    path('tour_single', views.tour_single,name='tour_single'),

]
