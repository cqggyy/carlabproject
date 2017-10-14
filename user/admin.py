from django.contrib import admin
from .models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['id', 'username', 'first_name', 'last_name', 'is_active']


admin.site.register(UserProfile, UserProfileAdmin)