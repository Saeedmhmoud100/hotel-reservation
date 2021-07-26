from rest_framework import permissions, viewsets
from .serializers import AboutSerializers,FAQSerializers
from .models import About, FAQ

class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS or request.user.is_superuser)
    def has_object_permission(self, request, view, obj):
        return bool(request.method in permissions.SAFE_METHODS or request.user.is_superuser)

class AboutAPIViewSets(viewsets.ModelViewSet):
    queryset=About.objects.all().order_by('-id')
    serializer_class=AboutSerializers
    # permission_classes=[ReadOnly]
    

class FaqAPIViewSets(viewsets.ModelViewSet):
    queryset=FAQ.objects.all().order_by('-id')
    serializer_class=FAQSerializers
    # permission_classes=[ReadOnly]