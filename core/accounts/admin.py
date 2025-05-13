from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Profile

# Register your models here.
# admin.site.register(User)


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_superuser", "is_active", "is_verified")
    list_filter = ("email", "is_superuser", "is_active", "is_verified")
    searching_fields = ("email",)
    ordering = ("email",)
    # user show only
    fieldsets = (
        (
            "Authentication",
            {
                "fields": ("email", "password"),
            },
        ),
        (
            "Permissions",
            {
                "fields": ("is_staff", "is_active", "is_superuser", "is_verified"),
            },
        ),
        (
            "Group Permissions",
            {
                "fields": ("groups", "user_permissions"),
            },
        ),
        (
            "Important date",
            {
                "fields": ("last_login",),
            },
        ),
    )
    # add new user fieldsets
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                ),
            },
        ),
    )


admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)
