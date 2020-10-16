from django.shortcuts import render, get_object_or_404
from .models import Posts


def index(request):
    posts = Posts.published.all()
    context = {
        'posts':posts,
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Posts, publish__year=year, publish__month=month, publish__day=day, slug=slug)
    context = {
        'post': post
    }
    return render(request, 'blog/single.html', context)
