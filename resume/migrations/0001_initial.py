# Generated by Django 3.1.2 on 2021-01-13 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('created_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'project',
            },
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, help_text='Category Name of the project', max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'ProjectCategory',
            },
        ),
        migrations.CreateModel(
            name='ResumeProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Full Name', max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('designation', models.CharField(blank=True, max_length=200, null=True)),
                ('career_goal', models.CharField(blank=True, max_length=500, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(blank=True, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('twitter_url', models.URLField(blank=True, null=True)),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('applicant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'ResumeProfile',
            },
        ),
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, help_text='Category Name of the skill', max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'SkillCategory',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Name of the skill', max_length=100, null=True)),
                ('skill_percentage', models.CharField(blank=True, help_text='Percentage of the skill', max_length=50, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_category', to='resume.skillcategory')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill', to='resume.resumeprofile')),
            ],
            options={
                'verbose_name_plural': 'Skill',
            },
        ),
        migrations.CreateModel(
            name='ResumeProfilePicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Name of the picture', max_length=100)),
                ('cover', models.ImageField(upload_to='profile_image/')),
                ('resume_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_picture', to='resume.resumeprofile')),
            ],
            options={
                'verbose_name_plural': 'ResumeProfilePicture',
            },
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_refree', models.CharField(max_length=100)),
                ('designation_of_refree', models.TextField()),
                ('phone_number', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reference', to='resume.resumeprofile')),
            ],
            options={
                'verbose_name_plural': 'reference',
            },
        ),
        migrations.CreateModel(
            name='ProjectPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Name of the picture', max_length=100)),
                ('cover', models.ImageField(upload_to='project_image/')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_picture', to='resume.project')),
            ],
            options={
                'verbose_name_plural': 'ProjectPicture',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_category', to='resume.projectcategory'),
        ),
        migrations.AddField(
            model_name='project',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='resume.resumeprofile'),
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('achievements', models.TextField(blank=True, null=True)),
                ('responsibilities', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='resume.resumeprofile')),
            ],
            options={
                'verbose_name_plural': 'Experience',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(help_text='Name of an institution', max_length=100)),
                ('location', models.CharField(help_text='Location of the institution', max_length=100)),
                ('result', models.CharField(help_text='Result', max_length=50)),
                ('course', models.CharField(help_text='Name of a course', max_length=200)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='resume.resumeprofile')),
            ],
            options={
                'verbose_name_plural': 'Education',
            },
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('organization', models.CharField(blank=True, max_length=500, null=True)),
                ('issue_date', models.DateField()),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('credential_id', models.CharField(blank=True, max_length=500, null=True)),
                ('credential_url', models.URLField(blank=True, null=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certification', to='resume.resumeprofile')),
            ],
            options={
                'verbose_name_plural': 'certification',
            },
        ),
        migrations.CreateModel(
            name='CertificatePicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Name of the picture', max_length=100)),
                ('cover', models.ImageField(upload_to='certificate_image/')),
                ('certificate_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificate_picture', to='resume.certification')),
            ],
            options={
                'verbose_name_plural': 'CertificatePicture',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('org_name', models.CharField(blank=True, max_length=500, null=True)),
                ('activity_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='resume.resumeprofile')),
            ],
            options={
                'verbose_name_plural': 'activity',
            },
        ),
    ]
