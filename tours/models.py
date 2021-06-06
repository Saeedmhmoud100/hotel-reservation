from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.


class Tour(models.Model):
    title = models.CharField(max_length = 150)
    price = models.PositiveIntegerField()
    country = models.ForeignKey('place', on_delete=models.CASCADE)
    locality =models.CharField(max_length=50)
    street = models.CharField(max_length = 150)
    descriptions = RichTextField()
    img = models.ImageField(upload_to='rooms/')
    days_number = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
class place(models.Model):
    place = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)