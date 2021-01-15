from django.shortcuts import render
from django.views import View
from django.conf import settings
from resume.models import ResumeProfilePicture,ResumeProfile
from django.shortcuts import get_object_or_404
from django.http import Http404

class HomeView(View):
    template_name = "home/index.html"
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        resume = get_object_or_404(ResumeProfile, pk=1)
        resume_pic = get_object_or_404(ResumeProfilePicture, pk=1)
        resume_pic_2 = get_object_or_404(ResumeProfilePicture, pk=2)
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            'resume_pic': resume_pic,
            'resume_pic_2': resume_pic_2,
            'resume': resume
        }
        return render(request, self.template_name, context)

