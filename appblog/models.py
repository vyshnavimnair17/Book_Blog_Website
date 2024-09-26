from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):  # main table
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    synopsis = models.TextField(default="synopsis")
    image = models.ImageField(upload_to='', default=1)
    description = models.TextField(default="description")
    genre = models.CharField(max_length=255, default="genre")

    class Meta:
        db_table = "cat_table"


class Current(models.Model):  # Currently Reading table under Category table
    cur_id = models.AutoField(primary_key=True)
    curr_read = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "current_table"


class Review(models.Model):  # Book review table
    rev_id = models.AutoField(primary_key=True)
    review = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "review_table"


class Wrapup(models.Model):  # Monthly wrapup table
    mon_id = models.AutoField(primary_key=True)
    month = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "wrapup_table"


class Recommendation(models.Model):  # recommendations table
    rec_id = models.AutoField(primary_key=True)
    recommend = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "recommendation_table"


class Tbr(models.Model):  # TBR list table
    tbr_id = models.AutoField(primary_key=True)
    toread = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "blogtable"


class Favourites(models.Model):
    fav_id = models.AutoField(primary_key=True)
    fav_read = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "fav_table"
