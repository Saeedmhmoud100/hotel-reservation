from django.db import models
from ckeditor.fields import RichTextField
from django_countries.fields import CountryField
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html
from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
class Room(models.Model):
    title = models.CharField(max_length = 150)
    price = models.PositiveIntegerField()
    total_rating = models.IntegerField(blank=True, null=True)
    country = CountryField()
    locality =models.CharField(max_length=50)
    street = models.CharField(max_length = 150)
    descriptions = RichTextField()
    img = models.ImageField(upload_to='rooms/')
    days_number = models.PositiveIntegerField()
    data_from = models.DateField(auto_now_add=True,blank=True)
    data_to = models.DateField(auto_now_add=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.title
    
    def img_tag(self):
        return format_html(
            "<img src='{}'  width='50' height='50' />",
            self.img.url,
        )
        
    def get_absolute_url(self):
        return reverse("rooms:hotel_room", kwargs={"pk": self.pk,'slug':self.slug})
        



class Room_image(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_img')
    img = models.ImageField(upload_to='rooms/')
    
    def image_preview(self):
        if self.img:
            return mark_safe(
            "<img src='{}'  width='100' height='70' />".format(self.img.url)
            )
        else:
            return '(No image)'
    
    def __str__(self):
        return str(self.room)


# class IntegerRangeField(models.IntegerField):
#     def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
#         self.min_value, self.max_value = min_value, max_value
#         models.IntegerField.__init__(self, verbose_name, name, **kwargs)
#     def formfield(self, **kwargs):
#         defaults = {'min_value': self.min_value, 'max_value':self.max_value}
#         defaults.update(kwargs)
#         return super(IntegerRangeField, self).formfield(**defaults)
    


class Room_Rating(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='rating', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='rating', on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    
    def __str__(self):
        return f'{self.room.title} - rating'
    
    
    
class Room_Reservation(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='room_Reservation', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='room_Reservation', on_delete=models.CASCADE)
    name = models.CharField(max_length=90)
    email_registered = models.EmailField()
    email_entred = models.EmailField()
    Data_from = models.DateField()
    Data_to = models.DateField()
    guste = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(6)])
    children = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(6)])
    price = models.IntegerField()
    canceled = models.BooleanField(default=False)
    done = models.BooleanField(default=False)