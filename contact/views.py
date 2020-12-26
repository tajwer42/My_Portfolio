from django.shortcuts import render

def my_contact(request):
    return render(request, 'contact/contact.html', {})