from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(('email address'), unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'


