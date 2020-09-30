from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    posts = Post.published.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, publish__year=year, publish__month=month, publish__day=day, post=post)
    context = {
        'post': post
    }
    return render(request, 'blog/single.html', context)
