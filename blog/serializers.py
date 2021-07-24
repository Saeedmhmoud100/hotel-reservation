from rest_framework import serializers
from .models import Categorie, Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Post
        fields='__all__'


class CategorieSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Categorie
        fields='__all__'

