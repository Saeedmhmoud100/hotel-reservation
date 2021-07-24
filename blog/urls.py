"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from . import views
from . import api_views
app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(),name='blog'),
    path('<slug:slug>/detail/', views.BlogDetailView.as_view(),name='blog-detail'),
    path('create/', views.BlogCreateView.as_view(),name='blog-create'),
    path('<slug:slug>/update/', views.BlogUpdateView.as_view(),name='blog-update'),
    path('<slug:slug>/delete/', views.BlogDeleteView.as_view(),name='blog-delete'),
    #APi
    path('api/list/', api_views.PostListAPIView.as_view(),name='post-list-api'),
    path('api/list/<int:pk>/', api_views.PostDetailAPIView.as_view(),name='post-detail-api'),
    path('api/list/search/<str:query>/', api_views.post_search_api,name='post-search-api'),
    
]