# Generated by Django 3.1.2 on 2021-01-07 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0017_auto_20210108_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumeprofilepricture',
            name='cover',
            field=models.ImageField(upload_to='profile_image/'),
        ),
    ]
