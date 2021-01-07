# Generated by Django 3.1.2 on 2021-01-06 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_auto_20210107_0246'),
    ]

    operations = [
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
        ),
    ]