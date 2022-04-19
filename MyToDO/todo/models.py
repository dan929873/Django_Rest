from django.db import models

from user.models import User


class Project(models.Model):
    name =  models.CharField(max_length=32)
    link =  models.CharField(max_length=100)
    users = models.ManyToManyField(User)

class TODO(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    note_text = models.TextField()
    data_create = models.DateField()
    data_cheng = models.DateField()
    user_created = models.OneToOneField(User, on_delete=models.CASCADE)
    activ = models.BooleanField()

    def save(self, *args, **kwargs):
        super(TODO, self).save(*args, **kwargs)

