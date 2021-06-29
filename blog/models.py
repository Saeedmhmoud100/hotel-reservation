from django.db import models
from django.shortcuts import reverse
from django.utils.safestring import mark_safe
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.template.defaultfilters import slugify, truncatechars
# Create your models here.

class PostManager(models.Manager):
    def active(self):
        return self.get_queryset().filter(active=True)
class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length = 30)
    img = models.ImageField(upload_to='blog/')
    tags = TaggableManager()
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE )
    description = RichTextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=True)
    objects=PostManager()
    def save(self,*args, **kwargs) :
        if self.title:
            self.slug = slugify(f'{self.pk}-{self.title}')
        super(Post,self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['-id']
        
    def show_img(self):
        return mark_safe(
            f"<img src='{self.img.url}'  width='50' height='50' />"
        )
        
    def sourt_description(self):
        return truncatechars(mark_safe(self.description),150)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:blog-detail", kwargs={"slug": self.slug})
    def get_update_url(self):
        return reverse('blog:blog-update',kwargs={'slug':self.slug})
    
    
    
class Categorie(models.Model):
    title = models.CharField(max_length=25)
    
    def __str__(self):
        return self.title