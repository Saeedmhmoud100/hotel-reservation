from django.db.models.query_utils import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Categorie, Post
from .serializers import CategorieSerializers, PostSerializers
from .permissions import IsStaffUser,IsAuthorOrReadOnly


class PostListAPIView(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializers
    # permission_classes = [IsStaffUser]

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializers
    # permission_classes = [IsAuthorOrReadOnly]


@api_view(['GET'])
def post_search_api(request,query):
    posts=Post.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query) 
    )
    data = PostSerializers(posts,many=True,context={'request':request}).data
    return Response({'data':data})


class CategorieListAPIView(generics.ListCreateAPIView):
    queryset=Categorie.objects.all()
    serializer_class=CategorieSerializers
    # permission_classes=[IsStaffUser]

class CategorieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Categorie.objects.all()
    serializer_class=CategorieSerializers
    # permission_classes=[IsStaffUser]

@api_view(['GET'])
def categorie_search_api(request,query):
    categories=Categorie.objects.filter(
        Q(title__icontains=query)
    )
    data = CategorieSerializers(categories,many=True).data
    return Response({'data':data})
