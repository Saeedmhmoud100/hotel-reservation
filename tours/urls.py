from django.urls import path
from . import views

app_name = 'tours'

urlpatterns = [
    # tour_list url
    path('', views.TourListView.as_view(),name='tour'),
    #tour_detail url
    path('<slug:slug>/detail/', views.TourDetailView.as_view(),name='tour_detail'),

]
