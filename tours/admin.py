from django.contrib import admin
from .models import Tour,Tour_image,Tour_Reservation,Tour_Rating
# Register your models here.


class Tour_imageAdmin(admin.TabularInline):
    model = Tour_image
    max_num = 4
    readonly_fields=('image_preview',)


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    inlines=[Tour_imageAdmin]
    list_display=('title','image_preview','city', 'locality', 'days_number', 'update_at','total_rating','check_avablity')
    readonly_fields = ['created_at']
    search_fields =['title','city__place','locality']
    class Meta:
        model = Tour
        fields = '__all__'

@admin.register(Tour_Reservation)
class Tour_ReservationAdmin(admin.ModelAdmin):
    list_display=['user','tour','email','data_from','data_to','canceled','done']
    list_editable = ('canceled','done')
    search_fields = ('user__username','tour__title','email','data_from','data_to','price')
    class Meta:
        model = Tour_Reservation
        fields = '__all__'


@admin.register(Tour_Rating)
class Tous_RatingAdmin(admin.ModelAdmin):
    list_display = ( "user",'shourt_feedback', "tour","rating")
