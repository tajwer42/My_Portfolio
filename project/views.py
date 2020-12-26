from django.shortcuts import render

def my_projects(request):
    return render(request, 'project/portfolio.html', {})
