from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.db.models.aggregates import Count
from .models import Categorie, Post
# Create your views here.
class BlogListView(ListView):
    model = Post
    paginate_by=1
    
    
class BlogDetailView(DetailView):
    model=Post
    
    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all().annotate(posts=Count('post'))
        return context