from django.contrib import admin
from main.models import Place,Category

# Register your models here.


@admin.register(Place)
class placeAdmin(admin.ModelAdmin):
    list_display = ( "name","created_at",)
    search_fields = ('place',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category
        fields = '__all__'
