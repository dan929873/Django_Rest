from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # username = models.CharField(max_length=64)
    # firstname = models.CharField(max_length=64)
    # lastname = models.CharField(max_length=64)
    email = models.EmailField(('email address'), unique=True)

