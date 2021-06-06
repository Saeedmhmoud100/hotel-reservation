from django.db.models.signals import pre_save,post_save
from django.template.defaultfilters import slugify
from ..models import Tour,Tour_image

def tour_slug(sender,instance,*args,**kwargs):
    instance.slug = slugify(f'{instance.pk}-{instance.title}')
    
    
def tour_img(sender,instance,*args,**kwargs):
    if instance.tour_img.filter(tour=instance):
        if not instance.tour_img.filter(img=instance.img).exists():
            l = instance.tour_img.all().first()
            l.img = instance.img
            l.save()
            
    else:
        instance.room_img.create(room=instance,img=instance.img)
    
    
pre_save.connect(tour_slug, sender=Tour)
post_save.connect(tour_img,sender=Tour)
