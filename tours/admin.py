from django.contrib import admin
from .models import Tour,Place
# Register your models here.


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    class Meta:
        model = Tour
        fields = '__all__'


@admin.register(Place)
class placeAdmin(admin.ModelAdmin):
    list_display = ( "place","created_at",)
