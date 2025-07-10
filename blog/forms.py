from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from blog.models import Blog, CustomUser, Profile, Comment


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
        fields = ('username', 'phone')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)
        labels = {
            'message': ''
        }
        widgets = {
            'message':
                forms.Textarea(
                    attrs={
                        'class': 'form-control',
                        'rows': 3,
                        'placeholder': "Write a message",
                        'aria-label': "Recipient's username",
                        'aria-describedby': "button-addon2",

                    })}