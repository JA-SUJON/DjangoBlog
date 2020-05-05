from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name    = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.TextField()

