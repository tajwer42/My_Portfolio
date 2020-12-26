from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.my_blogs, name='my_blogs'),
    path('blog/blog_single/', views.my_blog_singles, name='my_blog_singles'),
]
