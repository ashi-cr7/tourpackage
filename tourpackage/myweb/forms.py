from django import forms
from .models import *
from django.contrib.auth.models import User




class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user','tour_package']

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['name','description']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('booking','amount')

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('name', 'email', 'phone', 'address')        