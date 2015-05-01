from django.contrib import admin
from cowork.models import Address, Vat, Company, Location, Desk
# Register your models here.

admin.site.register(Address)
admin.site.register(Vat)
admin.site.register(Company)
admin.site.register(Location)
admin.site.register(Desk)