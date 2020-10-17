from django.urls import path
from .views import index, post_detail, about, contact, blogs

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', post_detail, name='post_detail'),
    path('about/', about ,name='about'),
    path('contact/', contact, name='contact'),
    path('blogs/',blogs, name='blog')
]
