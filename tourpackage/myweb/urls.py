from django.urls import path
from .import views as v
 

urlpatterns = [

path('', v.home, name='home'),
path('about/', v.about, name='about'),
path('admin/', v.admin_dashboard, name='admin'),
path('index/', v.index, name='index'),
path('base/', v.base, name='base'),
path('booking/', v.booking, name='booking'),
path('register/', v.register, name='register'),
path('login/', v.userlogn, name='userlogn'),
path('logout/', v.logout, name='uslogout'),
path('dashboard/', v.vendor_dashboard, name='dashboard'),
path('Package/', v.Package, name='Package'),
path('payment/<str:payment_id>/', v.payment, name='payment'),
path('contact/', v.contact, name='contact'),
path('vendor/', v.vendor, name='vendor'),
path('vendor_login/', v.vendor_login, name='vendor_login'),
 path('vendor_logout/', v.vendor_logout, name='vendor_logout'),

]