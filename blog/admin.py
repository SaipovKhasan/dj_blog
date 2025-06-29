from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm

from blog.forms import CustomUserCreationForm

from blog.models import Blog, CustomUser

admin.site.register(Blog)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # model = CustomUser
    # add_form = CustomUserCreationForm
    list_display = ['username', 'email', 'is_staff', 'phone', 'date_joined', 'id']
    list_display_links = ['username', 'phone', 'id']

    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("phone",)}),
    )
    add_fieldsets = (
        ('Create User groups', {
            "classes": ("wide",),
            "fields": ("username", "email", "phone", "password1", "password2")}
         ),
    )
