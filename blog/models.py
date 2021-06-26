from django.db import models
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.template.defaultfilters import slugify
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length = 30)
    img = models.ImageField(upload_to='blog/')
    tags = TaggableManager()
    description = RichTextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=True)
    
    def save(self,*args, **kwargs) :
        if self.title:
            self.slug = slugify(f'{self.pk}-{self.title}')
        super(Post,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title