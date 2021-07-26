from rest_framework import serializers
from .models import Newsletter_Email, Info

class NewsletterEmailSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Newsletter_Email
        fields='__all__'


class InfoSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Info
        fields='__all__'

