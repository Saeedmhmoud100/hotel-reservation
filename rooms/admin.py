from django.contrib import admin
from .models import Room,Room_image,Room_Rating
from .db.model import Active_Room
# Register your models here.



class Room_imageAdmin(admin.TabularInline):
    model = Room_image
    max_num = 4
    readonly_fields = ('image_preview',)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [Room_imageAdmin]
    list_display = ('title','img_tag','country', 'locality', 'days_number', 'update_at','total_rating' )
    readonly_fields = ['created_at']
    search_fields = ('title','descriptions')
    class Meta:
        model = Room
        fields = '__all__'


# @admin.register(Room_image)
# class Room_imageAdmin(admin.ModelAdmin):
#     list_display = ('room','img_tag')
#     class Meta:
#         model = Room_image
#         fields = '__all__'


class Active_RoomAdmin(admin.ModelAdmin):
    list_display = ('title','country','locality', 'update_at','total_rating','active')
    list_editable = ('active',)
    def get_queryset(self, request):
        return self.model.objects.active()
    class Meta:
        model = Active_Room


admin.site.register(Active_Room,Active_RoomAdmin)


class Room_RatingAdmin(admin.ModelAdmin):
    list_display = ('room','user','rating')
    class Meta:
        model = Room_Rating

admin.site.register(Room_Rating,Room_RatingAdmin)
