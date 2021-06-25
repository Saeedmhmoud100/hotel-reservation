from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.template.defaultfilters import slugify, truncatechars

# Create your models here.


class Tour(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length = 150)
    price = models.PositiveIntegerField()
    city = models.ForeignKey('place', on_delete=models.CASCADE)
    locality =models.CharField(max_length=50)
    street = models.CharField(max_length = 150)
    descriptions = RichTextField()
    img = models.ImageField(upload_to='rooms/')
    days_number = models.PositiveIntegerField()
    data_from = models.DateField(blank=True)
    data_to = models.DateField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=True)
    
    def save(self,*args, **kwargs):
        if self.title:
            self.slug = slugify(f'{self.pk}-{self.title}')  
        super(Tour, self).save(*args, **kwargs)
    @property
    def total_rating(self):
        rating_count= self.rating.all()
        rating = 0
        for i in rating_count:
            rating += i.rating
        if rating_count.exists():
            return int(rating/len(rating_count))
        return '0'
    @property
    def check_avablity(self):
        all_reservations = self.tour_Reservation.all()
        now = timezone.now().date()
        for reservation in all_reservations:
            if now > reservation.data_to : 
                return 'Avialable'

            elif now > reservation.data_from and now < reservation.data_to:
                reserved_to = reservation.data_to
                return f'In Progress to {reserved_to}'
        else:
            return 'Avialable'
        
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
    def get_update_url(self):
        return reverse('tours:tour-update',kwargs={'slug':self.slug})
    def get_delete_url(self):
        return reverse('tours:tour-delete',kwargs={'slug':self.slug})
    def get_reservation_url(self):
        return '{}#reservation_form'.format(reverse("tours:tour_detail", kwargs={'slug':self.slug}))

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
    
class Tour_Reservation_Manager(models.Manager):
    def is_active(self):
        return self.get_queryset().filter(canceled=False,done=False)
    
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
    objects = Tour_Reservation_Manager()
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return f'{self.tour.title} Reservation'
    
    
class Tour_Rating(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='tour_rating', on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, related_name='rating', on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    feedback = models.TextField(blank=True, null=True)
    
    def shourt_feedback(self):
        return truncatechars(self.feedback,150)  if self.feedback else '-'
    def __str__(self):
        return f'{self.tour.title} - rating'
    