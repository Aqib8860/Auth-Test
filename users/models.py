from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=25)
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=25)
    mobile = models.CharField(max_length=12)
    description = models.TextField()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
