from django.urls import path
from .views import index, post_detail

urlpatterns = [
    path('', index, name='index'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail')
]
