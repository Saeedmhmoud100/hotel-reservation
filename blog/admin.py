from django.contrib import admin
from .models import Post,Categorie
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','show_img','sourt_description','categorie','updated_at','active')
    list_editable=('active',)
    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    class Meta:
        model = Categorie
        fields = '__all__'
