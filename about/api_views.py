from rest_framework import permissions, viewsets
from .serializers import AboutSerializers
from .models import About

class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS or request.user.is_superuser)
    def has_object_permission(self, request, view, obj):
        return bool(request.method in permissions.SAFE_METHODS or request.user.is_superuser)
class AboutAPIViewSets(viewsets.ModelViewSet):
    queryset=About.objects.all().order_by('-id')
    serializer_class=AboutSerializers
    permission_classes=[ReadOnly]