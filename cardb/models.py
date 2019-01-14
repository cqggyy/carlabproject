from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Carmaker(models.Model):
    name = models.CharField(max_length=40, unique=True)
    name_cn = models.CharField(max_length=100, blank=True)
    logo = models.CharField(max_length=250, blank=True)
    country = models.CharField(max_length=30, blank=True)
    status = models.BooleanField(default=1)
    create_year = models.CharField(max_length=4, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carmakers')
    updated_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return self.name

class Carmodel(models.Model):
    name = models.CharField(max_length=40)
    name_cn = models.CharField(max_length=100, blank=True)
    carmaker = models.ForeignKey(Carmaker, on_delete=models.CASCADE, related_name='carmodels')
    generation = models.CharField(max_length=2, blank=True)
    platform = models.CharField(max_length=10, blank=True)
    picturename = models.CharField(max_length=250, blank=True)
    releaseyear = models.CharField(max_length=4, blank=True)
    endyear = models.CharField(max_length=4, blank=True)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carmodels')
    updated_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return self.name

class Carbodytype(models.Model):
    name = models.CharField(max_length=40)
    name_cn = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carbodytypes')
    updated_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return self.name

class Pttype(models.Model):
    name = models.CharField(max_length=40)
    name_cn = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pttypes')
    updated_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=40)
    name_cn =models.CharField(max_length=100, blank=True)
    carmaker = models.ForeignKey(Carmaker, on_delete=models.CASCADE, related_name='cars')
    carmodel = models.ForeignKey(Carmodel, on_delete=models.CASCADE, related_name='cars')
    carbodytype = models.ForeignKey(Carbodytype, on_delete=models.CASCADE, related_name='cars')
    brochurename = models.CharField(max_length=250, blank=True)
    picturename = models.CharField(max_length=250, blank=True)
    modelyear = models.CharField(max_length=4, blank=True)
    releasedate = models.DateField(blank=True)
    enddate = models.DateField(blank=True)
    wheelbase = models.CharField(max_length=5, blank=True)
    ftrack = models.CharField(max_length=4, blank=True)
    rtrack = models.CharField(max_length=4, blank=True)
    length = models.CharField(max_length=5, blank=True)
    width = models.CharField(max_length=5, blank=True)
    height = models.CharField(max_length=4, blank=True)
    clearance = models.CharField(max_length=4, blank=True)
    marketlocation = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    updated_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return self.name

class Cartrim(models.Model):
    name = models.CharField(max_length=40)
    name_cn = models.CharField(max_length=100, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='cartrims')
    carmodel = models.ForeignKey(Carmodel, on_delete=models.CASCADE, related_name='cartrims')
    pttype = models.ForeignKey(Pttype, on_delete=models.CASCADE, related_name='cartrims')
    drivetype = models.CharField(max_length=10, blank=True)
    maxspeed = models.CharField(max_length=5, blank=True)
    enginename = models.CharField(max_length=20, blank=True)
    engine_modelno = models.CharField(max_length=5, blank=True)
    enginecc = models.CharField(max_length=5, blank=True)
    engine_maxpower = models.CharField(max_length=4, blank=True)
    engine_maxnm = models.CharField(max_length=4, blank=True)
    transmissionname = models.CharField(max_length=10, blank=True)
    fueltype = models.CharField(max_length=20, blank=True)
    wheelbase = models.CharField(max_length=5, blank=True)
    ftrack = models.CharField(max_length=4, blank=True)
    rtrack = models.CharField(max_length=4, blank=True)
    length = models.CharField(max_length=5, blank=True)
    width = models.CharField(max_length=5, blank=True)
    height = models.CharField(max_length=4, blank=True)
    clearance = models.CharField(max_length=4, blank=True)    
    gvw = models.CharField(max_length=6, blank=True)    
    curbweight = models.CharField(max_length=6, blank=True)
    fweight = models.CharField(max_length=6, blank=True)
    rweight = models.CharField(max_length=6, blank=True)
    mpg = models.CharField(max_length=4, blank=True)
    tire = models.CharField(max_length=20, blank=True)
    wheel = models.CharField(max_length=20, blank=True)
    turncircle = models.CharField(max_length=5, blank=True)
    steerradio = models.CharField(max_length=5, blank=True)
    esc = models.CharField(max_length=20, blank=True)
    price = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cartrims')
    updated_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='+')