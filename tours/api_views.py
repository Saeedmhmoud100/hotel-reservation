from rest_framework import viewsets
from .serializers import TourSerializers,TourReservationSerializers,TourRatingSerializers
from .permissions import IsOwnerOrReadOnly, IsOwnerUserOrReadOnly, IsStaffUser
from .models import Tour, Tour_Rating, Tour_Reservation


class TourAPIViewSets(viewsets.ModelViewSet):
    queryset=Tour.objects.filter(active=True)
    serializer_class=TourSerializers
    # permission_classes=[IsStaffUser,IsOwnerOrReadOnly]
    search_fields = ['$title', '$descriptions']    

class TourReservationAPIViewSets(viewsets.ModelViewSet):
    queryset=Tour_Reservation.objects.all()
    serializer_class=TourReservationSerializers  
    # permission_classes=[IsOwnerUserOrReadOnly]
    filterset_fields=('user','tour')
    search_fields = ['$name', '$email_registered','$email_entred']
    
class TourRatingAPIViewSets(viewsets.ModelViewSet):
    queryset=Tour_Rating.objects.all()
    serializer_class=TourRatingSerializers
    # permission_classes=[IsOwnerUserOrReadOnly]
    filterset_fields=('user','tour')