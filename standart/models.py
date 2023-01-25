from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

#
# class Teg(models.Model):
#     name = models.CharField()
#
#
# class Event(models.Model):
#     time = models.DateTimeField()
#     user = models.Model()
#     event_type = models.TextField()
#     content = models.TextField()





