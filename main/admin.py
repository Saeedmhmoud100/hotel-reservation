from django.contrib import admin
from main.models import Place,Category,Home_Cart

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


@admin.register(Home_Cart)
class Home_CartAdmin(admin.ModelAdmin):
    class Meta:
        model = Home_Cart
        fields = '__all__'
