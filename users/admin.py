from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Add 'role' to the fieldsets (for editing)
    fieldsets = UserAdmin.fieldsets + (
        ('Role Information', {'fields': ('role',)}),
    )
    # Add 'role' to the list display in the admin table
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
