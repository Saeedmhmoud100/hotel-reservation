from django.db.models.query_utils import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import Newsletter_Email,Info
from .serializers import NewsletterEmailSerializers, InfoSerializers


class NewsletterEmailAPIViewSets(viewsets.ModelViewSet):
    queryset=Newsletter_Email.objects.all()
    serializer_class=NewsletterEmailSerializers

class InfoAPIViewSets(viewsets.ModelViewSet):
    queryset=Info.objects.all()
    serializer_class=InfoSerializers
