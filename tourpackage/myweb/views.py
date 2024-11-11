from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
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
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        myuser = User.objects.create_user(username,email,password)
        myuser.save
        return redirect('vendor_login')
    return render(request, 'vendor.html',)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('vendor_login')
        else:
            return redirect('vendor')
    return render(request, 'vendor_login.html')

def logout_view(request):
    logout(request)
    return redirect('vendor_login')

def contact(request):
    return render(request, 'contact.html') 

def user_dashboard(request):
    user = request.user
    bookings = Booking.objects.filter(user=user)

    return render(request, 'user_dashboard.html', {'bookings': bookings})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        myuser = User.objects.create_user(username,email,password)
        myuser.save
        return redirect('login')
    return render(request, 'register.html',)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('login')
        else:
            return redirect('regiter')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

def booking_success(request):
    return render(request, 'booking_success.html')

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})

def package(request):
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('package')
    else:
        form = PackageForm()
    return render(request, 'package.html', {'form': form})

def package_details(request, pk):
    package = Package.objects.get(pk=pk)
    return render('package_details.html',{'package':package})



def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            msg = form.cleaned_data['msg']
            return redirect('home')
    else:
        form = PaymentForm()
        return render(request,'payment.html',{'form':form}) 