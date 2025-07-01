from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from blog.models import Blog, CustomUser, Profile


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


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'phone',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)
