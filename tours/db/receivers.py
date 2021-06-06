from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from ..models import Tour

def tour_slug(sender,instance,*args,**kwargs):
    instance.slug = slugify(f'{instance.pk}-{instance.title}')
    
pre_save.connect(tour_slug, sender=Tour)

