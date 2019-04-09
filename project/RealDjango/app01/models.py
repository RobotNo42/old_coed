from django.db import models

# Create your models here.


class Vip(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)


class Boy(models.Model):
    name = models.CharField(max_length=32)


class Girl(models.Model):
    nick = models.CharField(max_length=32)


class Love(models.Model):
    b = models.ForeignKey('Boy', on_delete=None)
    g = models.ForeignKey('Girl', on_delete=None)


class happy(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField()
    choice = (
        (1, '男'),
        (2, '女')
    )
    sex = models.IntegerField(choices=choice, default=1)


class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
