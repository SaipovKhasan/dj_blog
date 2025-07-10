from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from blog.models import Blog, CustomUser, Profile, Comment

admin.site.register([Profile, Comment])


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
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