from rest_framework import viewsets
from .serializers import TourSerializers
from .models import Tour


class TourAPIViewSets(viewsets.ModelViewSet):
    queryset=Tour.objects.filter(active=True)
    serializer_class=TourSerializers