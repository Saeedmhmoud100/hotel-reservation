from django.contrib import admin
from main.models import Place

# Register your models here.


@admin.register(Place)
class placeAdmin(admin.ModelAdmin):
    list_display = ( "name","created_at",)
    search_fields = ('place',)
