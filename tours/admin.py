from django.contrib import admin
from .models import Tour,place
# Register your models here.


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    class Meta:
        model = Tour
        fields = '__all__'


@admin.register(place)
class placeAdmin(admin.ModelAdmin):
    list_display = ( "place","created_at",)
