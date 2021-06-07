
def nav_links(request):
    urlpath = request.path
    cxt = {
        'urlpath':urlpath,
    }
    return cxt