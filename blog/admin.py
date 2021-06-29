from django.contrib import admin
from .models import Post,Categorie
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','show_img','sourt_description','categorie','active')
    list_editable=('active',)
    search_fields = ['title','description','categorie__title','tags__name']
    list_filter=['active','tags','categorie','created_at','updated_at']
    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    search_fields=['title','post__title',]
    class Meta:
        model = Categorie
        fields = '__all__'
