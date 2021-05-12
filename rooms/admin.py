from django.contrib import admin
from .models import Room,Room_image
# Register your models here.


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('title','created_at')
    class Meta:
        model = Room
        fields = '__all__'


@admin.register(Room_image)
class Room_imageAdmin(admin.ModelAdmin):
    class Meta:
        model = Room_image
        fields = '__all__'
