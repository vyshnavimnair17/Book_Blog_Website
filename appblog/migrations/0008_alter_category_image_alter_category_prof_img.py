# Generated by Django 5.1.1 on 2024-10-04 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0007_favourites_review_recommendation_review_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='category',
            name='prof_img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
