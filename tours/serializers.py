from rest_framework import serializers
from .models import Tour,Tour_Reservation

class TourSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Tour
        fields='__all__'

class TourReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Tour_Reservation
        fields='__all__'
