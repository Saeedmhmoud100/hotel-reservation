from rest_framework import viewsets
from django_filters import rest_framework as filters
from .permissions import IsStaffUser,IsOwnerOrReadOnly
from .serializers import RoomSerializers
from .models import Room


class RoomAPIViewSets(viewsets.ModelViewSet):
    queryset=Room.objects.filter(active=True)
    serializer_class=RoomSerializers
    permission_classes=[IsStaffUser,IsOwnerOrReadOnly]
    search_fields = ['$title', '$descriptions']