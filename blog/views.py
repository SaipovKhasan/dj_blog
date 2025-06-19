import random
from dataclasses import dataclass

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound
from blog.models import Blog
from .models import Post


@dataclass
class Students:
    first_name: str
    last_name: str
    phone: str
    payed: bool


#
# st1 = Students('Alisher', 'Eshmatov', '998 91 903 34-43', True)
# st2 = Students('Alex', 'Gorden', '998 91 903 34-43', False)
# st3 = Students('Avazbek', 'Boymuradov', '998 90 903 00-42', True)
# st4 = Students('Abror', 'Sotiboldiyev', '998 33 300 40-43', True)
# students = [st1, st2, st3, st4]


def home(request):
    context = {
        "blogs": Blog.objects.all()
    }
    return render(request, template_name='blog/home.html', context=context)


def about(request):
    context = {
    }
    return render(request, template_name='blog/about.html', context=context)


def detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if not blog:
        return HttpResponseNotFound("Blog not found")
    context = {
        'blog': blog
    }
    return render(request, 'blog/detail.html', context=context)
