from django.urls import path
from . import views


app_name = 'rooms'

urlpatterns = [
    #room list url
    path('', views.HotelListView.as_view(),name='hotel'),
    #room detail urls
    path('room/<slug:slug>/', views.HotelRoomView.as_view(),name='hotel_room'),
    path("room_rating/", views.room_rate, name="room-rating"),
    #create new room url
    path("rooms/create/", views.HotelCreateView.as_view(), name="new-room"),
    #update room url
    path("room/<slug:slug>/update", views.HotelUpdateView.as_view(), name="update_room"),
    path("room/<slug:slug>/delete", views.HotelDeleteView.as_view(), name="delete_room"),

]
