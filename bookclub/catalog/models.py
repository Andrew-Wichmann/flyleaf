from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author')

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)