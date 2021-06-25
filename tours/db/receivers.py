from django.db.models.signals import post_save
from ..models import Tour

    
def tour_img(sender,instance,*args,**kwargs):
    if instance.tour_img.filter(tour=instance):
        if not instance.tour_img.filter(img=instance.img).exists():
            l = instance.tour_img.all().first()
            l.img = instance.img
            l.save()
            
    else:
        instance.tour_img.create(tour=instance,img=instance.img)
    
    
post_save.connect(tour_img,sender=Tour)
