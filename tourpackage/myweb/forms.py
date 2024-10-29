from django import forms
from .models import *
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','first_name']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')

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