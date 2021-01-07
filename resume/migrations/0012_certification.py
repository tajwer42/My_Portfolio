# Generated by Django 3.1.2 on 2021-01-07 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0011_auto_20210107_0252'),
    ]

    operations = [
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
                'verbose_name_plural': 'reference',
            },
        ),
    ]