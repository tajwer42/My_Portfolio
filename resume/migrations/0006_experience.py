# Generated by Django 3.1.2 on 2021-01-06 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_education_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='resume.resumeprofile')),
            ],
            options={
                'verbose_name_plural': 'Experience',
            },
        ),
    ]