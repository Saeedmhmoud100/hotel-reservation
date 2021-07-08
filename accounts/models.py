from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.utils.html import format_html
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


def get_profile_image_filepath(self, filename):
	return 'profile_images/' + str(self.pk) +  ' - ' + str(self.username) + '/profile_image.png'

class User(AbstractUser):
    image = models.ImageField(upload_to=get_profile_image_filepath,blank=True)
    country = CountryField(blank=True)
    city = models.CharField(max_length = 150,blank=True)
    phone_number = PhoneNumberField(blank=True)
    last_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)
    
    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index('profile_images/' + str(self.pk) +  ' - ' + str(self.username) + "/"):]
    
    def save(self,*args, **kwargs):
        if self.username:
            self.slug = slugify(self.username)  
        super(User, self).save(*args, **kwargs)
    
	
