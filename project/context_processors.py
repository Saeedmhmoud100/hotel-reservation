
from main.models import Info


def nav_links(request):
    urlpath = request.path
    cxt = {
        'urlpath':urlpath,
    }
    return cxt

def myfooter(request):
    info = Info.objects.last()
    cxt = {
        'myfooter':info,
    }
    return cxt