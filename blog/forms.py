from django import forms
from blog.models import Blog


class BlogForms(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'type', 'image', 'is_active']
