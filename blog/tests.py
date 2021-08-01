from django.conf import settings
from django.http import HttpResponseForbidden
from django.test import TestCase, testcases
from django.contrib.auth import get_user_model
from django.urls import reverse,resolve
from .models import Post,Categorie
from .views import BlogCreateView, BlogDeleteView, BlogDetailView, BlogListView, BlogUpdateView
from .forms import BlogForm
from django.core.files.uploadedfile import SimpleUploadedFile
# Create your tests here.


User = get_user_model()

class TestBlogModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',password='12345678Tests')
        self.categorie=Categorie.objects.create(title='test categorie')
        self.post = Post.objects.create(id=1,author=self.user,title='test post',categorie=self.categorie,description=('test posts'*50),img='blog/img1.jpg')
    
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
        
class TestBlogViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',password='12345678Tests')
        self.categorie=Categorie.objects.create(title='test categorie')
        self.post = Post.objects.create(author=self.user,title='test post',categorie=self.categorie,description=('test posts'*50),img='blog/img1.jpg')
        

    def test_post_list(self):
        url=reverse('blog:blog')
        response =self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(self.client.get(url+"?q=test").status_code,200)
        self.assertTemplateUsed(response,'blog/post_list.html')
    
    def test_post_detail(self):
        url=reverse('blog:blog-detail',args=[self.post.slug])
        response =self.client.get(url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/post_detail.html')

class TestBlogCreateView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',password='12345678Tests')
        self.categorie=Categorie.objects.create(title='test categorie')
        self.post = Post.objects.create(author=self.user,title='test post',categorie=self.categorie,description=('test posts'*50),img='blog/img1.jpg')
        
    def test_post_create_GET(self):
        user = self.user
        user.is_superuser = True
        user.save()
        self.client.force_login(user)
        response =self.client.get('/blog/create/')
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/post_form.html')
        self.assertContains(response,'New Post')
        
    def test_post_create_POST_Forbidden(self):
        self.client.force_login(self.user) 
        response =self.client.post('/blog/create/',{
            'title':'test form',
            'tags':'test,form',
            'categorie':self.categorie,
            'description':'test form description',
            'img':SimpleUploadedFile(name='test_image.jpg', content=open(str(settings.BASE_DIR) +'/static/images/bg_1.jpg' , 'rb').read(), content_type='image/jpeg')
        },follow=True)
        self.assertEquals(response.status_code,HttpResponseForbidden.status_code)
    
    def test_post_create_POST(self):
        user = self.user
        user.is_superuser = True
        user.save()
        self.client.force_login(user)
        response =self.client.post('/blog/create/',{
            'title':'test form',
            'img':SimpleUploadedFile(name='test_image.jpg', content=open(str(settings.BASE_DIR) +'/static/images/bg_1.jpg' , 'rb').read(), content_type='image/jpeg'),
            'tags':'test,form',
            'categorie':self.categorie.id,
            'description':'test form description',
        })
        self.assertEquals(response.status_code,302)
        self.assertEquals(Post.objects.first().title,'test form')
        self.assertEquals(Post.objects.count(),2)
        self.assertRedirects(response,reverse('blog:blog-detail',args=['2-test-form']))
            
            
class TestBlogUpdateView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',password='12345678Tests')
        self.categorie=Categorie.objects.create(title='test categorie')
        self.post = Post.objects.create(author=self.user,title='test post',categorie=self.categorie,description=('test posts'*50),img='blog/img1.jpg')
        self.update_url = reverse('blog:blog-update',args=[self.post.slug])
    def test_post_update_GET(self):
        user = self.user
        user.is_superuser = True
        user.save()
        self.client.force_login(user)
        response =self.client.get(self.update_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/post_form.html')
        self.assertContains(response,'Update Post')
        
    def test_post_update_POST_Forbidden(self):
        self.client.force_login(self.user) 
        response =self.client.post(self.update_url,{
            'title':'test form',
            'tags':'test,form',
            'categorie':self.categorie,
            'description':'test form description',
            'img':SimpleUploadedFile(name='test_image.jpg', content=open(str(settings.BASE_DIR) +'/static/images/bg_1.jpg' , 'rb').read(), content_type='image/jpeg')
        },follow=True)
        self.assertEquals(response.status_code,HttpResponseForbidden.status_code)
    
    def test_post_update_POST(self):
        user = self.user
        user.is_superuser = True
        user.save()
        self.client.force_login(user)
        response =self.client.post(self.update_url,{
            'title':'test form update',
            'img':SimpleUploadedFile(name='test_image.jpg', content=open(str(settings.BASE_DIR) +'/static/images/bg_1.jpg' , 'rb').read(), content_type='image/jpeg'),
            'tags':'test,form',
            'categorie':self.categorie.id,
            'description':'test form description',
        })
        self.assertEquals(response.status_code,302)
        self.assertEquals(Post.objects.first().title,'test form update')
        self.assertEquals(Post.objects.count(),1)
        self.assertRedirects(response,reverse('blog:blog-detail',args=['1-test-form-update']))
            
class TestBlogDeleteView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',password='12345678Tests')
        self.categorie=Categorie.objects.create(title='test categorie')
        self.post = Post.objects.create(author=self.user,title='test post',categorie=self.categorie,description=('test posts'*50),img='blog/img1.jpg')
        self.delete_url = reverse('blog:blog-delete',args=[self.post.slug])
    def test_post_delete_GET(self):
        user = self.user
        user.is_superuser = True
        user.save()
        self.client.force_login(user)
        response =self.client.get(self.delete_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/post_confirm_delete.html')
        self.assertContains(response,'Delete-test post')
        
    def test_post_delete_POST_Forbidden(self):
        self.client.force_login(self.user) 
        response =self.client.post(self.delete_url,{
            'title':'test form',
            'tags':'test,form',
            'categorie':self.categorie,
            'description':'test form description',
            'img':SimpleUploadedFile(name='test_image.jpg', content=open(str(settings.BASE_DIR) +'/static/images/bg_1.jpg' , 'rb').read(), content_type='image/jpeg')
        },follow=True)
        self.assertEquals(response.status_code,HttpResponseForbidden.status_code)
    
    def test_post_delete_POST(self):
        user = self.user
        user.is_superuser = True
        user.save()
        self.client.force_login(user)
        response =self.client.post(self.delete_url)
        self.assertEquals(response.status_code,302)
        self.assertEquals(Post.objects.count(),0)
        self.assertRedirects(response,reverse('blog:blog'))
            
class TestBlogForms(TestCase):
    def test_post_form(self):
        categorie=Categorie.objects.create(title='test categorie')
        form = BlogForm(data={
            'title':'test form',
            'tags':'test,form',
            'categorie':categorie,
            'description':'test form description'
        },files={
            'img':SimpleUploadedFile(name='test_image.jpg', content=open(str(settings.BASE_DIR) +'/static/images/bg_1.jpg' , 'rb').read(), content_type='image/jpeg')
        })
        self.assertTrue(form.is_valid())
    