from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class User(AbstractUser):
    img = models.ImageField(upload_to='accounts/',blank=True)
    country = CountryField(blank=True)
    city = models.CharField(max_length = 150,blank=True)
    phone_number = PhoneNumberField(blank=True)
    last_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)
    def save(self,*args, **kwargs):
        if self.username:
            self.slug = slugify(self.username)  
        super(User, self).save(*args, **kwargs)
    