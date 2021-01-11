from django.shortcuts import render
from resume.models import ResumeProfilePicture,ResumeProfile,Skill,SkillCategory, Certification,Education,Experience,Project,Certification

def my_about(request):
    resume = ResumeProfile.objects.get(pk=1)
    resume_pic = ResumeProfilePicture.objects.get(pk=2)
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    skills = Skill.objects.all()
    categories = SkillCategory.objects.all()
    projects = Project.objects.all()
    certifications =Certification.objects.all()
    context = {
            'resume_pic': resume_pic,
            'resume': resume,
            'educations': educations,
            'experiences': experiences,
            'skills': skills,
            'categories': categories,
            'projects': projects,
            'certifications': certifications
        }
    return render(request, 'resume/about.html', context)
