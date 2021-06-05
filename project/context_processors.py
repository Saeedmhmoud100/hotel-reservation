
def nav_links(request):
    home,about,room,tour,blog,content = '','','','','',''
    if request.path == '/': home='active'
    elif 'about' in request.path: about='active'
    elif 'hotel' in request.path: room='active'
    elif 'tour' in request.path: tour='active'
    elif 'blog' in request.path: blog='active'
    elif 'content' in request.path: content='active'
    cxt = {
        'home':home,
        'about':about,
        'room':room,
        'tour':tour,
        'blog':blog,
        'content':content,
        
    }
    return cxt