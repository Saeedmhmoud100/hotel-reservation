from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.
class BlogListView(ListView):
    model = Post
    paginate_by=1
def blog_single(request):
    return render(request,'blog/blog-single.html')