from django import template
from rooms.models import Room,Room_Rating
register = template.Library()

@register.simple_tag
def minus_one(num):
    rate = 1
    if Room.objects.filter(rating__room=num).exists():
        rate = Room.objects.get(pk=num).total_rating
    return rate

@register.simple_tag
def user_rating_numper(room,num):
    room = Room.objects.get(pk=room)
    rate = room.rating.filter(rating=num)
    return rate.count()

@register.filter
def for_loop(count,star_num):
    if int(count)< star_num: return True
    else: return False

@register.filter
def room_rating_chekd(user_and_room,room):
    try:
        if Room_Rating.objects.filter(user=user_and_room[0],room__pk=user_and_room[1]).exists:
            if Room_Rating.objects.get(user=user_and_room[0],room__pk=user_and_room[1]).rating == room:
                return True
    except:
        return False
    return False


@register.filter
def check_users_for_new_room(user):
    if user.is_authenticated:
        if user.is_superuser or user.is_staff:
            return True
    else:
        return False
    
@register.filter
def check_users_for_update_room(user):
    if user.is_authenticated:
        if user.is_superuser or user.is_staff:
            return True
    else:
        return False