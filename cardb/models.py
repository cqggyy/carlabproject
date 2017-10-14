from django.db import models


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=20)
    name_cn = models.CharField(max_length=100, blank=True)
    logo = models.CharField(max_length=250, blank=True)
    country = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=1)
    create_year = models.CharField(max_length=4, blank=True)

    def __str__(self):
        return self.name


class Carmodel(models.Model):
    name = models.CharField(max_length=20)
    name_cn = models.CharField(max_length=40, blank=True)
    manufacturer = models.ForeignKey(Manufacturer)
    modelyear = models.CharField(max_length=4, blank=True)
    platform = models.CharField(max_length=10, blank=True)
    picturename = models.CharField(max_length=250, blank=True)
    brochurename = models.CharField(max_length=250, blank=True)
    releasedate = models.DateField(blank=True)
    marketlocation = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=20)
    name_cn = models.CharField(max_length=40, blank=True)
    manufacturer = models.ForeignKey(Manufacturer)
    carmodel = models.ForeignKey(Carmodel)
    modelyear = models.CharField(max_length=4, blank=True)
    picturename = models.CharField(max_length=250, blank=True)
    brochurename = models.CharField(max_length=250, blank=True)
    bodytype = models.CharField(max_length=20, blank=True)
    drivetype = models.CharField(max_length=20, blank=True)
    wheelbase = models.CharField(max_length=6, blank=True)
    ftrack = models.CharField(max_length=5, blank=True)
    rtrack = models.CharField(max_length=5, blank=True)
    length = models.CharField(max_length=5, blank=True)
    width = models.CharField(max_length=5, blank=True)
    height = models.CharField(max_length=5, blank=True)
    curbweight = models.CharField(max_length=5, blank=True)
    gvw = models.CharField(max_length=5, blank=True)
    enginetype = models.CharField(max_length=10, blank=True)
    enginecc = models.CharField(max_length=5, blank=True)
    engineliter = models.CharField(max_length=5, blank=True)
    enginepercyl = models.CharField(max_length=2, blank=True)
    engineinj = models.CharField(max_length=10, blank=True)
    engineintake = models.CharField(max_length=2, blank=True)
    enginecylcontrol = models.CharField(max_length=10, blank=True)
    enginestoke = models.CharField(max_length=20, blank=True)
    ratio = models.CharField(max_length=10, blank=True)
    hp = models.CharField(max_length=5, blank=True)
    h_rpm = models.CharField(max_length=5, blank=True)
    nm = models.CharField(max_length=5, blank=True)
    t_npm = models.CharField(max_length=5, blank=True)
    trans = models.CharField(max_length=20, blank=True)
    fueltype = models.CharField(max_length=2, blank=True)
    esc = models.CharField(max_length=2, blank=True)
    mpg = models.CharField(max_length=10, blank=True)
    price = models.CharField(max_length=10, blank=True)