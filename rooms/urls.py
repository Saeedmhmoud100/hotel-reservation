from django.urls import path
from . import views


app_name = 'rooms'

urlpatterns = [
    path('', views.home,name='home'),
    path('hotel', views.HotelListView.as_view(),name='hotel'),
    path('hotel/room/<int:pk>/<slug:slug>/', views.HotelRoomView.as_view(),name='hotel_room'),
    path('tour', views.tour,name='tour'),
    path('tour_single', views.tour_single,name='tour_single'),

]
