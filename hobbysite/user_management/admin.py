from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(UserAdmin):
    model = Profile
    list_display = ['username', 'email', 'display_name', 'first_name', 'last_name', 'is_active', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('display_name',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('display_name',)}),
    )
