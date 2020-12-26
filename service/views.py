from django.shortcuts import render

def my_service(request):
    return render(request, 'service/services.html', {})
