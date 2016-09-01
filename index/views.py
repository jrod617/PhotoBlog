from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from photoOnlyPost import views as getPosts
from photoOnlyPost.forms import PhotoForm

def index(request):
    posts = getPosts.getRandomPosts(30)
    form = PhotoForm()
    return render(request, 'index/index.html', {'posts' : posts, 'form': form } )