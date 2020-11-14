from django.shortcuts import render, get_object_or_404
from .models import Posts
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.http import JsonResponse


def index(request):
    posts_list = Posts.published.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 2)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Posts, publish__year=year, publish__month=month, publish__day=day, slug=slug)
    context = {
        'post': post
    }
    return render(request, 'blog/blog-single.html', context)


def blogs(request):
    posts_list = Posts.published.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 6)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
    }
    return render(request, 'blog/blog.html', context)


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    if request.method == 'POST' and request.is_ajax:
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_mail(subject, f"Name: {name}\nEmail: {email}\nMessage: {message}", email, ['testingblog260@gmail.com'],
                  fail_silently=True)
        return JsonResponse({'response': 'success'}, status=200)
    return render(request, 'blog/contact.html')
