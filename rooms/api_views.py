from rest_framework import viewsets
from .permissions import IsOwnerUserOrReadOnly, IsStaffUser,IsOwnerOrReadOnly
from .serializers import RoomSerializers,RoomRatingSerializers,RoomReservationSerializers
from .models import Room, Room_Rating, Room_Reservation


class RoomAPIViewSets(viewsets.ModelViewSet):
    queryset=Room.objects.filter(active=True)
    serializer_class=RoomSerializers
    permission_classes=[IsStaffUser,IsOwnerOrReadOnly]
    search_fields = ['$title', '$descriptions']
    
class RoomRatingAPIViewSets(viewsets.ModelViewSet):
    queryset=Room_Rating.objects.all()
    serializer_class=RoomRatingSerializers
    permission_classes=[IsOwnerUserOrReadOnly]
    filterset_fields=('user','room')
    
class RoomReservationAPIViewSets(viewsets.ModelViewSet):
    queryset=Room_Reservation.objects.all()
    serializer_class=RoomReservationSerializers
    permission_classes=[IsOwnerUserOrReadOnly]
    filterset_fields=('user','room')
    search_fields = ['$name', '$email_registered','$email_entred']
    