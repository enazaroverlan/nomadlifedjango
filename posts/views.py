from django.shortcuts import render
from .models import Post
# Create your views here.


def PostView(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    template = 'Posts/post_home.html'
    return render(request, template, context)