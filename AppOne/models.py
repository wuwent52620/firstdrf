from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)

class Group(models.Model):
    num = models.IntegerField()