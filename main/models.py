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
