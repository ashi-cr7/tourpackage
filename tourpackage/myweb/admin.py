from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Booking, Package

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('id', 'date_joined')

class BookingAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'tour_package', 'tour_date', 'num_travelers')
    search_fields = ('user__username', 'package__name')

class PackageAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'description', 'price', 'duration', 'destination')
    search_fields = ('name', 'description')

admin.site.register(User, CustomUserAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Package, PackageAdmin)
