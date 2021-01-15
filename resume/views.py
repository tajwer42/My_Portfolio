from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from resume.models import (
    ResumeProfilePicture,ResumeProfile,SkillCategory,
    Certification,Education,Experience,CertificatePicture,
    Activity,ProjectCategory
)

def my_about(request):
    resume = get_object_or_404(ResumeProfile, pk=1)
    resume_pic = get_object_or_404(ResumeProfilePicture, pk=1)
    resume_pic_2 = get_object_or_404(ResumeProfilePicture, pk=2)
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    skill_categories = SkillCategory.objects.all()
    projects_catagories = ProjectCategory.objects.all()
    certifications =Certification.objects.all()
    activity = Activity.objects.all()
    context = {
            'resume_pic': resume_pic,
            'resume_pic_2': resume_pic_2,
            'resume': resume,
            'educations': educations,
            'experiences': experiences,
            'skill_categories': skill_categories,
            'projects_catagories': projects_catagories,
            'certifications': certifications,
            'activity': activity
        }
    return render(request, 'resume/about.html', context)
