from django.db import models
from django.contrib.auth.models import User
from .constant import GENDER_TYPE

class Useraccount(models.Model):
    user = models.OneToOneField(User, related_name="account", on_delete=models.CASCADE)
    balance = models.DecimalField(default=0,max_digits=12,decimal_places=2)
    gender = models.CharField(max_length=100,choices=GENDER_TYPE)
    def __str__(self) -> str:
        return str(self.user.username)
    

class UserAddress(models.Model):
    user = models.OneToOneField(User,related_name='address',on_delete=models.CASCADE)
    post_code = models.IntegerField()
    city = models.CharField(max_length=200)
    current_address = models.CharField(max_length=200)
    ccuntry = models.CharField(max_length=200)


