from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class Movie(models.Model):
#     title = models.CharField(max_length=45)
#     description = models.TextField()
#     release_date = models.DateTimeField()
#     duration = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
