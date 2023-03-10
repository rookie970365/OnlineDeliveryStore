from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminGeneric

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = "pk", "user", "info"

