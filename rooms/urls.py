from django.urls import path
from . import views


app_name = 'rooms'

urlpatterns = [
    #home page url
    path('', views.home,name='home'),
    #room list url
    path('hotel/', views.HotelListView.as_view(),name='hotel'),
    #room detail urls
    path('hotel/room/<int:pk>/<slug:slug>/', views.HotelRoomView.as_view(),name='hotel_room'),
    path("room_rating/", views.room_rate, name="room-rating"),
    #create new room url
    path("hotel/room/create/", views.HotelCreateView.as_view(), name="create-room"),
    path('tour', views.tour,name='tour'),
    path('tour_single', views.tour_single,name='tour_single'),

]
