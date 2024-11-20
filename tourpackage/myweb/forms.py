from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

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

class VendorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('company_name', 'address', 'phone', 'email')

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)        