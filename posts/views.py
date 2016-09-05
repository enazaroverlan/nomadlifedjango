from django.shortcuts import render
from .models import Post


# Create your views here.

def indexAction(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    template = 'Posts/index.html'
    return render(request, template, context)
