from django.contrib import admin
from .models import Post,Categorie
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    class Meta:
        model = Categorie
        fields = '__all__'
