from django.contrib.auth.models import AbstractUser
from django.db import models


class Blog(models.Model):
    TYPE = {
        'Journal': 'Journal',
        "Life updates": 'Life updates',
        'Travel stories': 'Travel stories',
        'Personal growth': 'Personal growth'
    }
    author = models.ForeignKey('blog.CustomUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Title')
    content = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    type = models.CharField(max_length=50, choices=TYPE, default='Journal')
    created_at = models.DateTimeField(auto_now_add=True)  # 2025-06-19 16:28
    updated_at = models.DateTimeField(auto_now=True)  # 2025-06-22 15:28

    def __str__(self):
        return f"{self.id} {self.title}"

    class Meta:
        permissions = [
            ('can_all_manage', 'Can all changed models')
        ]


class CustomUser(AbstractUser):
    phone = models.CharField(unique=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_img/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}, {self.user.phone}"
