from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255,null=True,blank=True)
         
class Package(models.Model):
    name = models.CharField(max_length=255, default=0)
    description = models.TextField(default=0)
    duration = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    destination = models.CharField(max_length=255)

class Booking(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255, default=0)
    email = models.EmailField(default=0)
    phone = models.CharField(max_length=20,default=0)

class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=200)
    card_number = models.CharField(max_length=200,default=0)
    expiration_date = models.DateField(default=0)
    cvv = models.CharField(max_length=100,default=0)


class Vendor(models.Model):
    Vendor_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255,default=0)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255,null=True)

    USERNAME_FIELD = 'default_username'

    def _str_(self):
        return self.vendor_name