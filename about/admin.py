from django.contrib import admin
from .models import About,FAQ

# Register your models here.


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    class Meta:
        model = About
        fields = '__all__'


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    class Meta:
        model = FAQ
        fields = '__all__'
