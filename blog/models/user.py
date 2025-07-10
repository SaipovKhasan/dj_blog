from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import AUTH_USER_MODEL


class CustomUser(AbstractUser):
    phone = models.CharField(unique=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_img/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}, {self.user.phone}"