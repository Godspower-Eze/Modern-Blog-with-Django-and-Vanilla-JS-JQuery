from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        queryset = super(PublishedManager, self).get_queryset()
        main = queryset.filter(status='Published')
        return main


class Post(models.Model):
    STATUS_CHOICES = (
        ('', ''),
        ('Published', 'Published'),
        ('Draft', 'Draft')
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    objects = models.Manager
    published = PublishedManager

    class Meta:
        ordering = ('-publish',)
