from rest_framework import viewsets
from .serializers import TourSerializers
from .permissions import IsOwnerOrReadOnly, IsStaffUser
from .models import Tour


class TourAPIViewSets(viewsets.ModelViewSet):
    queryset=Tour.objects.filter(active=True)
    serializer_class=TourSerializers
    permission_classes=[IsStaffUser,IsOwnerOrReadOnly]
    search_fields = ['$title', '$descriptions']    