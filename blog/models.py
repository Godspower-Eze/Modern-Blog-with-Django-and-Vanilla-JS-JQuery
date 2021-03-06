from django.db import models
from urllib.parse import quote_plus
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(default='default.png', upload_to='profile_images')

    def __str__(self):
        return self.user.username


class PublishedManager(models.Manager):
    def get_queryset(self):
        queryset = super(PublishedManager, self).get_queryset()
        main = queryset.filter(status='Published')
        return main


class Posts(models.Model):
    STATUS_CHOICES = (
        ('', ''),
        ('Published', 'Published'),
        ('Draft', 'Draft')
    )
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    featured_image = models.ImageField(blank=True, upload_to='featured_images')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = RichTextUploadingField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    @property
    def url_coded_string(self):
        return quote_plus(self.title)

    @property
    def monthpublished(self):
        return self.publish.strftime('%B')

    @property
    def post_author_image(self):
        return self.author.profile.user_image.url

    objects = models.Manager()
    published = PublishedManager()
