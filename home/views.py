from django.shortcuts import render
from django.views import View
from django.conf import settings
from resume.models import ResumeProfilePicture

class HomeView(View):
    model = ResumeProfilePicture
    template_name = "home/index.html"
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
        }
        return render(request, self.template_name, context)

