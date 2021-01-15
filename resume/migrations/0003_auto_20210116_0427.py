# Generated by Django 3.1.2 on 2021-01-15 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20210116_0419'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_name', models.CharField(blank=True, help_text='Sub Category Name of the project(webdevelpment/design)', max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'ProjectSubCategory',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_sub_category', to='resume.projectcategory'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectcategory',
            name='category_name',
            field=models.CharField(blank=True, help_text='Category Name of the project(personal/professional)', max_length=100, null=True),
        ),
    ]