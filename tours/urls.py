from django.urls import path
from . import views

app_name = 'tours'

urlpatterns = [
    path('', views.TourListView.as_view(),name='tour'),
    path('tour_single', views.tour_single,name='tour_single'),

]
