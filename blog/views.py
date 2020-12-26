from django.shortcuts import render

def my_blogs(request):
    return render(request, 'blog/blog_main.html', {})

def my_blog_singles(request):
    return render(request, 'blog/blog_single.html', {})
