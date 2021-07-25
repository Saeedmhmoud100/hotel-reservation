from rest_framework import serializers
from .models import Room,Room_Rating

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Room
        fields='__all__'

class RoomRatingSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Room_Rating
        fields='__all__'