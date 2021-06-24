from django.urls import path
from . import views

app_name = 'tours'

urlpatterns = [
    path('', views.TourListView.as_view(),name='tour'),
    path('<slug:slug>/detail/', views.TourDetailView.as_view(),name='tour_detail'),
    path("tour_rating/", views.tour_rate, name="tour-rating"),
    path('create/', views.CreateTourView.as_view(),name='new-tour'),
    path('<slug:slug>/update/', views.UpdateTourView.as_view(),name='tour-update'),
    path('<slug:slug>/delete/', views.DeleteTourView.as_view(),name='tour-delete'),
    
]
