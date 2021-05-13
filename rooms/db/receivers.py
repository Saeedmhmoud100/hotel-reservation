from django.db.models.signals import pre_save,post_save
from django.template.defaultfilters import slugify
from django.dispatch import receiver
from rooms.models import Room


def room_slug(sender,instance,*args,**kwargs):
    instance.slug = slugify(instance.title)
    
    
def room_img(sender,instance,*args,**kwargs):
    if not instance.room_img.filter(img=instance.img).exists():
        l = instance.room_img.all().first()
        l.img = instance.img
        l.save()
        


pre_save.connect(room_slug, sender=Room)
post_save.connect(room_img, sender=Room)