# Create your views here.

from django.shortcuts import render
from dimg.models import Post

def index(request):
    latest_entry_list = Post.objects.all().order_by('-created')[:5]
    context = {'latest_entry_list': latest_entry_list}
    return render(request, 'dimg/index.html', context)

def detail(request, entry_id):
    comic = Post.objects.get(id=entry_id)
    comic_comments = comic.comments
    context = {
            'comic_img': comic.image,
            'comic_comments': comic_comments,
            'comic': comic
    }
    return render(request, 'dimg/comic.html', context)
