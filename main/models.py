from django.db import models

# Create your models here.



class Place(models.Model):
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to='places/')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length = 100)
    icon = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Home_Cart(models.Model):
    title = models.CharField(max_length =30)
    text = models.CharField(max_length=200)
    icon = models.CharField(max_length=50)
    created_add = models.DateTimeField(auto_now=False)
    
    def __str__(self):
        return self.title
    class Meta:
        ordering=['-id']

class Newsletter_Email(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Newsletter_Email'
        verbose_name_plural = 'Newsletter_Emails'

    def __str__(self):
        return self.email
    
class Info(models.Model):
    site_name= models.CharField(max_length = 30)
    description = models.TextField(max_length=500)
    fb_url = models.URLField(max_length=200 , blank=True, null=True)
    twitter_url = models.URLField(max_length=200 , blank=True, null=True)
    Instgram_url = models.URLField(max_length=200 , blank=True, null=True)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    mail = models.EmailField( max_length=254)
    class Meta:
        verbose_name = ("Info")
        verbose_name_plural = ("Info")

    def __str__(self):
        return self.site_name
