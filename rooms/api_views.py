from rest_framework import viewsets
from .models import Room
from .serializers import RoomSerializers


class RoomAPIViewSets(viewsets.ModelViewSet):
    queryset=Room.objects.all()
    serializer_class=RoomSerializers
    