from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,default="")
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=5, choices=(("male","男"),("female","女")), default="female")
    address = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    headico = models.ImageField(upload_to="media/headico/%Y/%M", default="media/headico/default.png", max_length=100)
    class Meta:
        db_table = 'auth_user'
