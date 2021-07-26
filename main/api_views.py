from rest_framework import permissions, viewsets
from .models import Newsletter_Email,Info
from .serializers import NewsletterEmailSerializers, InfoSerializers

class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS or request.user.is_superuser)
    def has_object_permission(self, request, view, obj):
        return bool(request.method in permissions.SAFE_METHODS or request.user.is_superuser)

class CreateOnly(permissions.IsAuthenticated,ReadOnly):
    pass
class NewsletterEmailAPIViewSets(viewsets.ModelViewSet):
    queryset=Newsletter_Email.objects.all()
    serializer_class=NewsletterEmailSerializers
    permission_classes=[CreateOnly]

class InfoAPIViewSets(viewsets.ModelViewSet):
    queryset=Info.objects.all()
    serializer_class=InfoSerializers
    permission_classes=[ReadOnly]
