from django import forms
from django.contrib.auth.forms import UserCreationForm

from blog.models import Blog, CustomUser


class BlogForms(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'type', 'image', 'is_active']


class UserForms(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'is_staff', 'phone']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'phone', 'email']
