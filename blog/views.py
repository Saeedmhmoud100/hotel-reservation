from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post
# Create your views here.
class BlogListView(ListView):
    model = Post
    paginate_by=1
    
    
class BlogDetailView(DetailView):
    model=Post
    