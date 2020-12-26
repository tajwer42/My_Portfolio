from django.shortcuts import render

def my_about(request):
    return render(request, 'resume/about.html', {})
