from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.db.models.aggregates import Count
from taggit.models import Tag
from .models import Categorie, Post
# Create your views here.
class BlogListView(ListView):
    model = Post
    paginate_by=1
    
    def get_queryset(self):
        queryset = super(BlogListView, self).get_queryset() 
        if self.request.GET.get('tag',False):queryset=Post.objects.filter(tags__name=self.request.GET['tag'])
        return queryset
    
class BlogDetailView(DetailView):
    model=Post
    
    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all().annotate(posts=Count('post'))
        context['recent_posts'] = Post.objects.all()[:3]
        context['tags'] = tags = Tag.objects.all()
        return context