from django.db import models
from django.contrib.auth.models import User

class ResumeProfile(models.Model):
    applicant = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=False, help_text="Full Name")
    slug = models.SlugField(max_length=50, unique=True)
    designation = models.CharField(max_length=200, blank=True, null=True)
    career_goal=models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    email=models.EmailField(blank=False, null=False)
    website=models.URLField(blank=True, null=True)
    linkedin_url=models.URLField(blank=True, null=True)
    twitter_url=models.URLField(blank=True, null=True)
    facebook_url=models.URLField(blank=True, null=True)
    summary=models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ResumeProfile'

    def __str__(self):
        return self.name

class ResumeProfilePicture(models.Model):
    resume = models.ForeignKey(ResumeProfile, related_name='resume_picture',on_delete=models.CASCADE,)
    title = models.CharField(max_length=100, blank=False, null=False, help_text="Name of the picture")
    cover = models.ImageField(upload_to='profile_image/')

    class Meta:
        verbose_name_plural = 'ResumeProfilePicture'

    def __str__(self):
        return self.title

class Education(models.Model):
    resume = models.ForeignKey(ResumeProfile, related_name='education',on_delete=models.CASCADE,)
    institution_name = models.CharField(max_length=100, blank=False, null=False, help_text="Name of an institution")
    location = models.CharField(max_length=100, blank=False, null=False, help_text="Location of the institution")
    result = models.CharField(max_length=50, blank=False, null=False, help_text="Result")
    course = models.CharField(max_length=200, blank=False, null=False, help_text="Name of a course")
    description = models.CharField(max_length=400, blank=True, null=True)
    start_date = models.DateField() #only get year
    end_date = models.DateField() # only year

    class Meta:
        verbose_name_plural = 'Education'

    def __str__(self):
        return '{0} -> {1}'.format(self.resume.name, self.institution_name)

class Experience(models.Model):
    resume = models.ForeignKey(ResumeProfile, related_name='experience',on_delete=models.CASCADE,)
    designation = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    description=models.CharField(max_length=400, blank=True, null=True)
    achievements = models.TextField(blank=True, null=True)
    responsibilities = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural='Experience'

    def __str__(self):
        return self.company

class SkillCategory(models.Model):
    category_name = models.CharField(max_length=100, blank=True, null=True, help_text="Category Name of the skill")

    class Meta:
        verbose_name_plural='SkillCategory'
    
    def __str__(self):
        return self.category_name

class Skill(models.Model):
    resume=models.ForeignKey(ResumeProfile, related_name="skill",on_delete=models.CASCADE,)
    name = models.CharField(max_length=100, blank=True, null=True, help_text="Name of the skill")
    skill_percentage = models.CharField(max_length=50, blank=True, null=True, help_text="Percentage of the skill")
    category = models.ForeignKey(SkillCategory, related_name="skill_category",on_delete=models.CASCADE,)

    class Meta:
        verbose_name_plural='Skill'

    def __str__(self):
        return self.name

class Reference(models.Model):
    resume = models.ForeignKey(ResumeProfile, related_name='reference',on_delete=models.CASCADE,)
    name_of_refree=models.CharField(max_length=100, blank=False, null=False)
    designation_of_refree = models.TextField(blank=False, null=False)
    phone_number=models.CharField(max_length=50, blank=False, null=False)
    email=models.EmailField(blank=False, null=False)
    linkedin_url=models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural='reference'

    def __str__(self):
        return self.name_of_refree


class Certification(models.Model):
    resume = models.ForeignKey(ResumeProfile, related_name='certification',on_delete=models.CASCADE,)
    name = models.CharField(max_length=500, blank=False, null=False)
    organization = models.CharField(max_length=500, blank=True, null=True)
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)
    credential_id = models.CharField(max_length=500, blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural='certification'

    def __str__(self):
        return self.name

class CertificatePicture(models.Model):
    resume = models.ForeignKey(Certification, related_name='certificate_picture',on_delete=models.CASCADE,)
    title = models.CharField(max_length=100, blank=False, null=False, help_text="Name of the picture")
    cover = models.ImageField(upload_to='certificate_image/')

    class Meta:
        verbose_name_plural = 'CertificatePicture'

    def __str__(self):
        return self.title

class Project(models.Model):
    resume = models.ForeignKey(ResumeProfile, related_name='project',on_delete=models.CASCADE,)
    name = models.CharField(max_length=500, blank=False, null=False)
    created_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural='project'

    def __str__(self):
        return self.name

class ProjectPicture(models.Model):
    resume = models.ForeignKey(Project, related_name='project_picture',on_delete=models.CASCADE,)
    title = models.CharField(max_length=100, blank=False, null=False, help_text="Name of the picture")
    cover = models.ImageField(upload_to='project_image/')

    class Meta:
        verbose_name_plural = 'ProjectPicture'

    def __str__(self):
        return self.title

class Activity(models.Model):
    resume = models.ForeignKey(ResumeProfile, related_name='activity',on_delete=models.CASCADE,)
    name = models.CharField(max_length=500, blank=False, null=False)
    activity_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural='activity'

    def __str__(self):
        return self.name