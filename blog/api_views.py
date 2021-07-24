from django.shortcuts import get_object_or_404,get_list_or_404
from django.db.models.query_utils import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import PostSerializers
from .models import Post


class PostListAPIView(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializers

@api_view(['GET'])
def post_detail_api(request,id):
    post=get_object_or_404(Post,id=id)
    data = PostSerializers(post,context={'request':request}).data
    return Response({'data':data})

@api_view(['GET'])
def post_search_api(request,query):
    posts=Post.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query) 
    )
    data = PostSerializers(posts,many=True,context={'request':request}).data
    return Response({'data':data})