from django.db import models
from ckeditor.fields import RichTextField
from django_countries.fields import CountryField
from django.utils import timezone
from django.utils.html import format_html
from django.template.defaultfilters import truncatechars
# Create your models here.   

class Room(models.Model):
    title = models.CharField(max_length = 150)
    price = models.PositiveIntegerField()
    #rating
    country = CountryField()
    locality =models.CharField(max_length=50)
    street = models.CharField(max_length = 150)
    descriptions = RichTextField()
    img = models.ImageField(upload_to='rooms/')
    days_number = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def img_tag(self):
        return format_html(
            "<img src='{}'  width='50' height='50' />",
            self.img.url,
        )

class Room_image(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_img')
    img = models.ImageField(upload_to='rooms/')
    
    def img_tag(self):
        return format_html(
            "<img src='{}'  width='100' height='70' />",
            self.img.url,
        )
    
    def __str__(self):
        return str(self.room)

