from django.urls import path
from .views import index, post_detail

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', post_detail, name='post_detail')
]
