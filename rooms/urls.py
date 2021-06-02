from django.urls import path
from . import views


app_name = 'rooms'

urlpatterns = [
    #home page url
    path('', views.HomeView.as_view(),name='home'),
    #room list url
    path('hotel/', views.HotelListView.as_view(),name='hotel'),
    #room detail urls
    path('hotel/room/<slug:slug>/', views.HotelRoomView.as_view(),name='hotel_room'),
    path("room_rating/", views.room_rate, name="room-rating"),
    #create new room url
    path("hotel/rooms/create/", views.HotelCreateView.as_view(), name="new-room"),
    #update room url
    path("hotel/room/<slug:slug>/update", views.HotelUpdateView.as_view(), name="update_room"),
    path("hotel/room/<slug:slug>/delete", views.HotelDeleteView.as_view(), name="delete_room"),
    path('tour', views.tour,name='tour'),
    path('tour_single', views.tour_single,name='tour_single'),

]
