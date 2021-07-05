from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.HomeView.as_view(),name='home'),
    path('search/', views.places_search,name='search'),
    path('category/<str:category>/', views.category_filter,name='category_filter'),
    path('place/<str:place>/', views.place_filter,name='palce_filter'),
    path('news_letter_Subcriber/',views.news_letter_Subcriber,name='news_letter_Subcriber')
]
