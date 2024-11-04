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
path('login/', v.login_view, name='login'),
path('logout/', v.logout_view, name='uslogout'),
path('vendor/', v.vendor, name='vendor'),
path('package/', v.package, name='package'),
path('profile/', v.user_dashboard, name='profile'),
path('payment/', v.payment, name='payment'),
path('vendor/', v.vendor, name='vendor'),
path('contact/', v.contact, name='contact'),
]