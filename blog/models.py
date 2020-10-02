from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


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
    featured_image = models.ImageField(blank=True, upload_to='featured_images')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    objects = models.Manager()
    published = PublishedManager()
