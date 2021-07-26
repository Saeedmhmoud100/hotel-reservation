from rest_framework import serializers
from .models import About

class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model  = About
        fields='__all__'
