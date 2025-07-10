from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from blog.forms import CustomUserCreationForm  # ,  # CustomUserChangeForm
from blog.models import Blog, CustomUser, Profile

admin.site.register([Profile])


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # model = CustomUser
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    list_display = ['username', 'email', 'is_staff', 'phone', 'date_joined', 'id']
    list_display_links = ['username', 'phone', 'id']

    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {'fields': ('phone',)}),
    )

    add_fieldsets = (
        ("Create User groups", {
            'classes': ('wide',),
            'fields': ('username', "usable_password", 'phone', 'password1', 'password2')}
         ),
    )

# admin.site.register([CustomUser, CustomUserAdmin])