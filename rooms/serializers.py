from rest_framework import serializers
from .models import Room,Room_Rating,Room_Reservation

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Room
        fields='__all__'

class RoomRatingSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Room_Rating
        fields='__all__'
        
class RoomReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Room_Reservation
        fields='__all__'