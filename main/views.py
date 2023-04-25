from django.shortcuts import render
from comments.models import Post

# Create your views here.
def homeView(request):
    posts = Post.objects.all()
    context={
        'posts_set':posts
    }
    return render(request, 'home.html', context)