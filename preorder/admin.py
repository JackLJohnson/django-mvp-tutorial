from django.contrib import admin

from preorder.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email')


# Register your models here.
admin.site.register(Customer, CustomerAdmin)