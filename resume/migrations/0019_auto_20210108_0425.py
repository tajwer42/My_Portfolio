# Generated by Django 3.1.2 on 2021-01-07 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0018_auto_20210108_0416'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resumeprofilepricture',
            options={'verbose_name_plural': 'ResumeProfilePicture'},
        ),
        migrations.CreateModel(
            name='CertificatePricture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Name of the picture', max_length=100)),
                ('cover', models.ImageField(upload_to='certificate_image/')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificate_picture', to='resume.certification')),
            ],
            options={
                'verbose_name_plural': 'CertificatePicture',
            },
        ),
    ]
