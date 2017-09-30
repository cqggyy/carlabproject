from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=20)
    name_cn = models.CharField(max_length=100)
    logo = models.CharField(max_length=250)

class Carmodel(models.Model):
    name = models.CharField(max_length=20)
    name_cn = models.CharField(max_length=40)
    manufacturer = models.ForeignKey(Manufacturer)
    wheelbase = models.IntegerField(blank=True)
    ftrack = models.IntegerField(blank=True)
    rtrack = models.IntegerField(blank=True)

class Car(models.Model):
    name = models.CharField(max_length=20)
    name_cn = models.CharField(max_length=40)
    manufacturer = models.ForeignKey(Manufacturer)
    carmodel = models.ForeignKey(Carmodel)
