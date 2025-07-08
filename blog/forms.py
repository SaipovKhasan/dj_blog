from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from blog.models import Blog, CustomUser, Profile


class BlogForms(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'type', 'image', 'is_active']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'phone')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'phone', 'first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)