from rest_framework import viewsets
from .permissions import IsStaffUser,IsOwnerOrReadOnly
from .serializers import RoomSerializers
from .models import Room


class RoomAPIViewSets(viewsets.ModelViewSet):
    queryset=Room.objects.all()
    serializer_class=RoomSerializers
    permission_classes=[IsStaffUser,IsOwnerOrReadOnly]