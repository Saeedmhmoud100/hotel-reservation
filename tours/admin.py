from django.contrib import admin
from .models import Tour,Place,Tour_image
# Register your models here.


class Tour_imageAdmin(admin.TabularInline):
    model = Tour_image
    max_num = 4
    readonly_fields=('image_preview',)


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    inlines=[Tour_imageAdmin]
    list_display=('title','image_preview','city', 'locality', 'days_number', 'update_at')
    readonly_fields = ['created_at']
    class Meta:
        model = Tour
        fields = '__all__'

@admin.register(Place)
class placeAdmin(admin.ModelAdmin):
    list_display = ( "place","created_at",)
