from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name    = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.TextField()


class Category(models.Model):
    name    = models.CharField(max_length=100)


class Article(models.Model):
    article_author = models.ForeignKey(Author,on_delete=models.CASCADE)
    title          = models.CharField(max_length=200)
    body           = models.TextField()
    category       = models.ForeignKey(Category,on_delete=models.CASCADE)

