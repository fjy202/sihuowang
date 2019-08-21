"""
Definition of models.
"""

from django.db import models

# Create your models here.
class sihuo1(models.Model):
    fromuser=models.TextField(max_length=10)
    requires=models.TextField(max_length=500)
    title=models.TextField(max_length=20)
class Invitation(models.Model):
    fromuser=models.TextField(max_length=10)
    tousers=models.TextField(max_length=10)
    requires=models.TextField(max_length=500)
    title=models.TextField(max_length=20)
