from django.contrib import admin
from .models import Booking, Package


class BookingAdmin(admin.ModelAdmin):
    list_display = ( 'package', 'name', 'email', 'phone')
    search_fields = ('package', 'email')
class packageAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'description', 'duration','price','destination')
    search_fields = ('name', 'description')


admin.site.register(Booking, BookingAdmin)
admin.site.register(Package, packageAdmin)