from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.HomeView.as_view(),name='home'),
    path('search/', views.places_search,name='search'),
    path('category/<str:category>/', views.category_filter,name='category_filter'),
]
