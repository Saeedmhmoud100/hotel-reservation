from django import template
from ..models import Tour, Tour_Rating
register = template.Library()


@register.simple_tag
def user_rating_numper(tour,num):
    tour = Tour.objects.get(pk=tour)
    rate = tour.rating.filter(rating=num)
    return rate.count()

@register.filter
def for_loop(count,star_num):
    if int(count)< star_num: return True
    else: return False

@register.simple_tag
def tour_rating_chekd(user,tour,num):
    try:
        if Tour_Rating.objects.filter(user=user,tour__pk=tour).exists:
            if Tour_Rating.objects.get(user=user,tour__pk=tour).rating == num:
                return 'checked'
    except:
        return ''
    return ''
