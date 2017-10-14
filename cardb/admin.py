from django.contrib import admin
from .models import Manufacturer, Carmodel, Car

# Register your models here.


class ManufacturerAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'name_cn', 'create_year', 'status']

class CarmodelAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'name_cn', 'manufacturer', 'modelyear']

class CarAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'name_cn', 'carmodel', 'manufacturer', 'wheelbase', 'modelyear','price']



admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Carmodel, CarmodelAdmin)
admin.site.register(Car, CarAdmin)