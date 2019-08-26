from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
posts = [
    {
        'title': 'Mont Blac',
        'user': {
            'name': 'Tesica Cortes',
            'photo': 'https://picsum.photos/id/1/32/32'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/237/200/200'
    },
    {
        'title': 'Vía Lactea',
        'user': {
            'name': 'C. Vander',
            'photo': 'https://picsum.photos/id/2/32/32'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/236/200/200'
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name':'Thespianatist',
            'photo': 'https://picsum.photos/id/3/32/32'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/235/200/200'
    },
]

def list_posts(req):
    content = []
    #return HttpResponse(content)
    return render(req, 'feed.html', {'posts': posts})
