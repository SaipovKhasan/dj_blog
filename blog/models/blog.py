from django.db import models

from config.settings import AUTH_USER_MODEL


class Blog(models.Model):
    TYPE = {
        'Journal': 'Journal',
        "Life updates": 'Life updates',
        'Travel stories': 'Travel stories',
        'Personal growth': 'Personal growth'
    }
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Title')
    content = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    type = models.CharField(max_length=50, choices=TYPE, default='Journal')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.title}"

    class Meta:
        permissions = [
            ('can_all_manage', 'Can all changed models')
        ]


class Comment(models.Model):
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.author:
            return f"{self.author.username}: {self.message[:30]}"
        return f"{self.message[:30]}"

    class Meta:
        ordering = ['-created_at']
