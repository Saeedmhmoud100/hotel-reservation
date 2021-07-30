from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post,Categorie
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
        