from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Tour(models.Model):
    title = models.CharField(max_length = 150)
    price = models.PositiveIntegerField()
    city = models.ForeignKey('place', on_delete=models.CASCADE)
    locality =models.CharField(max_length=50)
    street = models.CharField(max_length = 150)
    descriptions = RichTextField()
    img = models.ImageField(upload_to='rooms/')
    days_number = models.PositiveIntegerField()
    data_from = models.DateField()
    data_to = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    def image_preview(self):
        if self.img:
            return mark_safe(
            "<img src='{}'  width='60' height='60' />".format(self.img.url)
            )
        else:
            return '(No image)'
        
    def get_absolute_url(self):
        return reverse('tours:tour_detail',kwargs={'slug':self.slug})
    class Meta:
        ordering=['-id']
    
class Place(models.Model):
    place = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.place
    
    
class Tour_image(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='tour_img')
    img = models.ImageField(upload_to='tour/',blank=True)
    
    def image_preview(self):
        if self.img:
            return mark_safe(
            "<img src='{}'  width='100' height='70' />".format(self.img.url)
            )
        else:
            return '(No image)'
    
    def __str__(self):
        return str(self.tour)
    
class Tour_Reservation(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='tour_Reservation', on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, related_name='tour_Reservation', on_delete=models.CASCADE)
    name = models.CharField(max_length=90)
    email = models.EmailField()
    data_from = models.DateField()
    data_to = models.DateField()
    guste = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(6)],blank=True)
    children = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(6)],blank=True)
    price = models.IntegerField()
    canceled = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-id']
    
    