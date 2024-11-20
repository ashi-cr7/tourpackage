from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255,default=0)
    groups = models.ManyToManyField('auth.Group', related_name='myweb_users')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='myweb_users')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255,null=True,blank=True)
         

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour_package = models.CharField(max_length=200)
    tour_date = models.DateField()
    num_travelers = models.IntegerField()

class Package(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Number of days")
    destination = models.CharField(max_length=200)

class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=255)
    payment_date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
