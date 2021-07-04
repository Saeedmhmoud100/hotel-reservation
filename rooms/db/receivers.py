from django.db.models.signals import pre_save,post_save
from django.template.defaultfilters import slugify
from rooms.models import Room,Room_Rating
from .model import Active_Room

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
    rating_count= Room_Rating.objects.filter(room=instance.room)
    rating = 0
    for i in rating_count:
        rating += i.rating
    if rating_count.exists():
        instance.room.total_rate=int(rating/len(rating_count))
    else:
        instance.room.total_rating = 0
    instance.room.save()


pre_save.connect(room_slug, sender=Room)
post_save.connect(room_img, sender=Room)
post_save.connect(room_img, sender=Active_Room)
post_save.connect(total_rating, sender=Room_Rating)
