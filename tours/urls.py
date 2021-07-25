from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
from .api_views import TourAPIViewSets, TourRatingAPIViewSets,TourReservationAPIViewSets

app_name = 'tours'

router = DefaultRouter()
router.register('tour',TourAPIViewSets)
router.register('reservation',TourReservationAPIViewSets)
router.register('rating',TourRatingAPIViewSets)

urlpatterns = [
    path('', views.TourListView.as_view(),name='tour'),
    path('<slug:slug>/detail/', views.TourDetailView.as_view(),name='tour_detail'),
    path("tour_rating/", views.tour_rate, name="tour-rating"),
    path('create/', views.CreateTourView.as_view(),name='new-tour'),
    path('<slug:slug>/update/', views.UpdateTourView.as_view(),name='tour-update'),
    path('<slug:slug>/delete/', views.DeleteTourView.as_view(),name='tour-delete'),
    
    #api
    path('api/',include(router.urls))
    
]
