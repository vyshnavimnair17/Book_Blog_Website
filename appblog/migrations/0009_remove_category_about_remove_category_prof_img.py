# Generated by Django 5.1.1 on 2024-10-07 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0008_alter_category_image_alter_category_prof_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='about',
        ),
        migrations.RemoveField(
            model_name='category',
            name='prof_img',
        ),
    ]
