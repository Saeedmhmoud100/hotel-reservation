from django.db.models.signals import pre_save,post_save
from django.template.defaultfilters import slugify
from django.dispatch import receiver
from rooms.models import Room


def room_slug(sender,instance,*args,**kwargs):
    instance.slug = slugify(f'{instance.pk}-{instance.title}')
    
    
def room_img(sender,instance,*args,**kwargs):
    if instance.room_img.filter(room=instance):
        if not instance.room_img.filter(img=instance.img).exists():
            l = instance.room_img.all().first()
            l.img = instance.img
            l.save()
            
    else:
        instance.room_img.create(room=instance,img=instance.img)
    
def total_rating(sender,instance,*args,**kwargs):
    if instance.rating.filter(room=instance).exists():
        count = int(instance.rating.all().count())
        rating = 0
        for i in instance.rating.all():
            rating += i.rating
        rating = rating / count
        instance.total_rating = rating
    else:
        instance.total_rating = 1


pre_save.connect(room_slug, sender=Room)
post_save.connect(room_img, sender=Room)
pre_save.connect(total_rating, sender=Room)
