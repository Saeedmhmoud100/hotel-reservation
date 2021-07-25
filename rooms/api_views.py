from rest_framework import viewsets
from .permissions import IsStaffUser,IsOwnerOrReadOnly
from .serializers import RoomSerializers,RoomRatingSerializers
from .models import Room, Room_Rating


class RoomAPIViewSets(viewsets.ModelViewSet):
    queryset=Room.objects.filter(active=True)
    serializer_class=RoomSerializers
    permission_classes=[IsStaffUser,IsOwnerOrReadOnly]
    search_fields = ['$title', '$descriptions']
    
class RoomRatingAPIViewSets(viewsets.ModelViewSet):
    queryset=Room_Rating.objects.all()
    serializer_class=RoomRatingSerializers