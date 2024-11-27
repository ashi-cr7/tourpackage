from django import forms
from .models import *
from .views import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.hashers import make_password

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserloginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address']




class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['name', 'description', 'duration', 'price','destination']    

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'package']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_method', 'card_number', 'expiration_date', 'cvv']
        

class VendorRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Vendor
        fields = ['Vendor_name', 'username', 'address', 'phone', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')

    def save(self, commit=True):
        vendor = super().save(commit=False)
        # Use make_password to hash the password
        vendor.password = make_password(self.cleaned_data['password'])
        if commit:
            vendor.save()
        return vendor
    
class VendorLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)