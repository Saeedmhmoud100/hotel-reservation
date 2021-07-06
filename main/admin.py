from django.contrib import admin
from main.models import Place,Category,Home_Cart,Newsletter_Email,Info

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


@admin.register(Newsletter_Email)
class Newsletter_EmailAdmin(admin.ModelAdmin):
    list_display=['email','created_at',]
    readonly_fields = ['created_at']    
    class Meta:
        model = Newsletter_Email
        fields = '__all__'


@admin.register(Info)
class MyFooterAdmin(admin.ModelAdmin):
    class Meta:
        model = Info
        fields = '__all__'
