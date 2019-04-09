from django.db import models

# Create your models here.


class Man(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    sex = models.CharField(max_length=16)


class Woman(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    sex = models.CharField(max_length=16)


class BtoG(models.Model):
    b = models.ForeignKey('Man', on_delete=None)
    g = models.ForeignKey('Woman', on_delete=None)