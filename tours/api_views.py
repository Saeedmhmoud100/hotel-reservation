from rest_framework import viewsets
from .serializers import TourSerializers,TourReservationSerializers
from .permissions import IsOwnerOrReadOnly, IsStaffUser
from .models import Tour, Tour_Reservation


class TourAPIViewSets(viewsets.ModelViewSet):
    queryset=Tour.objects.filter(active=True)
    serializer_class=TourSerializers
    permission_classes=[IsStaffUser,IsOwnerOrReadOnly]
    search_fields = ['$title', '$descriptions']    

class TourReservationAPIViewSets(viewsets.ModelViewSet):
    queryset=Tour_Reservation.objects.all()
    serializer_class=TourReservationSerializers  