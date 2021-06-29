from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls.base import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.db.models.aggregates import Count
from django.db.models.query_utils import Q
from taggit.models import Tag
from .models import Categorie, Post
from .forms import BlogForm

# Create your views here.
class BlogListView(ListView):
    model = Post
    paginate_by=1
    
    def get_queryset(self):
        queryset = super(BlogListView, self).get_queryset().filter(active=True)
        if self.request.GET.get('tag',False):queryset=Post.objects.active().filter(tags__name=self.request.GET['tag'])
        if self.request.GET.get('categorie',False): queryset=Post.objects.active().filter(categorie__title=self.request.GET['categorie'])
        if self.request.GET.get('q',False):
            q = self.request.GET['q']
            queryset=Post.objects.active().filter(Q(title__icontains=q)|Q(description__icontains=q))
        return queryset
    
class BlogDetailView(DetailView):
    model=Post
    
    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all().annotate(posts=Count('post'))
        context['recent_posts'] = Post.objects.active().exclude(pk=self.get_object().pk)[:3]
        context['tags'] = Tag.objects.all()
        return context
    
class BlogCreateView(UserPassesTestMixin,LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model= Post
    form_class = BlogForm
    success_message='Created Post Successfully!!'
    def form_valid(self,form):
        myform = form.save(commit=False)
        myform.author=self.request.user
        self.object=form.save()
        return super(BlogCreateView, self).form_valid(form)
    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        return False
class BlogUpdateView(UserPassesTestMixin,LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Post
    form_class= BlogForm
    success_message='Updated Post Successfully!!'
    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff and self.get_object().author==self.request.user:
            return True
        return False
class BlogDeleteView(UserPassesTestMixin,LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Post
    success_url=reverse_lazy('blog:blog')
    success_message='Deleted Post Successfully!!'
    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(BlogDeleteView, self).delete(request, *args, **kwargs)
    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff and self.get_object().author==self.request.user:
            return True
        return False
