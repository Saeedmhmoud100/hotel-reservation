from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .api_views import AboutAPIViewSets,FaqAPIViewSets
from . import views


app_name = 'about'

router = DefaultRouter()
router.register('tour',AboutAPIViewSets)
router.register('faq',FaqAPIViewSets)
urlpatterns = [
    path('', views.Aboutview.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    
    #api
    path('api/',include(router.urls))
    
]
