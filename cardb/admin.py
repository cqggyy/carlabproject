from django.contrib import admin
from .models import Carmaker, Carmodel, Car

# Register your models here.


class CarmakerAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'name_cn', 'create_year', 'status']

class CarmodelAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'name_cn', 'carmaker', 'releaseyear']

class CarAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'name_cn', 'carmodel', 'carmaker', 'wheelbase', 'modelyear','marketlocation']



admin.site.register(Carmaker, CarmakerAdmin)
admin.site.register(Carmodel, CarmodelAdmin)
admin.site.register(Car, CarAdmin)