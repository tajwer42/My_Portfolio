from django.contrib import admin
from resume import models

class ResumeProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)

class ResumeProfilePictureAdmin(admin.ModelAdmin):
    list_display = ('title',)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution_name','course',)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company','designation',)

class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name','category',)

class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('name_of_refree','email',)

class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name','organization',)

class CertificatePictureAdmin(admin.ModelAdmin):
    list_display = ('title',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','created_date',)

class ProjectPictureAdmin(admin.ModelAdmin):
    list_display = ('title',)

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name','activity_date',)

admin.site.register(models.ResumeProfile, ResumeProfileAdmin)
admin.site.register(models.ResumeProfilePicture, ResumeProfilePictureAdmin)
admin.site.register(models.Education, EducationAdmin)
admin.site.register(models.Experience, ExperienceAdmin)
admin.site.register(models.SkillCategory, SkillCategoryAdmin)
admin.site.register(models.Skill, SkillAdmin)
admin.site.register(models.Reference, ReferenceAdmin)
admin.site.register(models.Certification, CertificationAdmin)
admin.site.register(models.CertificatePicture, CertificatePictureAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.ProjectPicture, ProjectPictureAdmin)
admin.site.register(models.Activity, ActivityAdmin)