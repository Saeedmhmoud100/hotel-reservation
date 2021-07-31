from django.test import TestCase, testcases
from django.contrib.auth import get_user_model
from django.urls import reverse,resolve
from .models import Post,Categorie
from .views import BlogCreateView, BlogDeleteView, BlogDetailView, BlogListView, BlogUpdateView
# Create your tests here.

User = get_user_model()

class TestBlogModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',password='12345678Tests')
        self.categorie=Categorie.objects.create(title='test categorie')
        self.post = Post.objects.create(author=self.user,title='test post',categorie=self.categorie,description=('test posts'*50),img='blog/img1.jpg')
    
    def test_model_str(self):
        self.assertEqual(self.categorie.__str__(),self.categorie.title)
        self.assertEqual(self.post.__str__(),self.post.title)

    def test_model_maneger(self):
        self.assertEqual(Post.objects.active().count(),1)
        self.assertEqual(Post.objects.active().count(),Post.objects.filter(active=True).count())

    def test_model_methods(self):
        self.assertEqual(self.post.show_img(),"<img src='/media/blog/img1.jpg'  width='50' height='50' />")
        self.assertEqual(len(self.post.sourt_description()),150)

    def test_model_url(self):
        self.assertEqual(self.post.get_absolute_url(),'/blog/1-test-post/detail/')
        self.assertEqual(self.post.get_update_url(),'/blog/1-test-post/update/')
        self.assertEqual(self.post.get_delete_url(),'/blog/1-test-post/delete/')
        
class TestBlogUrls(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',password='12345678Tests')
        self.categorie=Categorie.objects.create(title='test categorie')
        self.post = Post.objects.create(author=self.user,title='test post',categorie=self.categorie,description=('test posts'*50),img='blog/img1.jpg')
    
    def test_post_list_urls(self):
        url = reverse('blog:blog')
        self.assertEqual(resolve(url).func.view_class,BlogListView)
        
    def test_post_detail_urls(self):
        url = reverse('blog:blog-detail',args=[self.post.slug])
        self.assertEqual(resolve(url).func.view_class,BlogDetailView)
    
    def test_post_create_urls(self):
        url = reverse('blog:blog-create')
        self.assertEqual(resolve(url).func.view_class,BlogCreateView)
    
    def test_post_update_urls(self):
        url = reverse('blog:blog-update',args=[self.post.slug])
        self.assertEqual(resolve(url).func.view_class,BlogUpdateView)
    
    def test_post_delete_urls(self):
        url = reverse('blog:blog-delete',args=[self.post.slug])
        self.assertEqual(resolve(url).func.view_class,BlogDeleteView)