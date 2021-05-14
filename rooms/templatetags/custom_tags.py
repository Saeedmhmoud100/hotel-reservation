from django import template
from rooms.models import Room
register = template.Library()

@register.simple_tag
def minus_one(num):
    rate = 1
    if Room.objects.filter(rating__room=num).exists():
        rate = Room.objects.get(pk=num).total_rating
    return rate
