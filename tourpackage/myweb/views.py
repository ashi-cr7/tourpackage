from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from .forms import *


# Create your views here.

def home (request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')

def vendor(request):
    if request.method == 'POST':
        form = VendorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor_login')
    else:
        form = VendorRegistrationForm()
    return render(request, 'vendor.html', {'form': form})

def vendor_login(request):
    if request.method == 'POST':
        form = VendorLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if Vendor.objects.get(username=username):
                return redirect('home')
    else:
        form = VendorLoginForm()
    return render(request, 'vendorlogin.html', {'form': form})

def vendor_logout(request):
    logout(request)
    return redirect('vendor_login')

def vendor_dashboard(request):
    return render(request, 'vendor_dashboard.html')


def contact(request):
    return render(request, 'contact.html') 


def register(request):
    if request.method == 'POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userlogn')
    else:
        form = UserRegisterForm()
    return render(request,"register.html",{'form':form})
    
def userlogn(request):
    if request.method == 'POST':
        form = UserloginForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                print(f"Authentication failed for username: {username}")
                form.add_error(None, "Incorrect username or password")
    else:
        form = UserloginForm()

    return render(request, "login.html", {'form': form})

def userlogout(request):
    logout(request)
    return redirect('home')                


def Package(request):
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking')
    else:
        form = PackageForm()
    return render(request, 'Package.html', {'form': form})
        

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

def payment(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if request.method == 'POST':
        form = paymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.booking = booking
            payment.save()
            return redirect('payment_success')
    else:
        form = paymentForm()
    return render(request, 'payment.html', {'form': form, 'booking': booking})