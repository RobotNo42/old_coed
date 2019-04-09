from django.db import models


class Class(models.Model):
    title = models.CharField(max_length=64)


class Student(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=64, null=True)
    age = models.CharField(max_length=32, null=True)
    class_price = models.CharField(max_length=64, null=True)
    cls = models.ForeignKey('Class', on_delete=None, null=True)


class Teacher(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    TtoC = models.ManyToManyField('Class')

