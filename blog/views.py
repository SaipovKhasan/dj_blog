import random
from dataclasses import dataclass

from django.shortcuts import render

from blog.models import Blog


@dataclass
class Students:
    first_name: str
    last_name: str
    phone: str
    payed: bool


st1 = Students('Alisher', 'Eshmatov', '998 91 903 34-43', True)
st2 = Students('Alex', 'Gorden', '998 91 903 34-43', False)
st3 = Students('Avazbek', 'Boymuradov', '998 90 903 00-42', True)
st4 = Students('Abror', 'Sotiboldiyev', '998 33 300 40-43', True)
students = [st1, st2, st3, st4]


def home(request):
    context = {
        "blogs": Blog.objects.all()
    }
    return render(request, template_name='blog/home.html', context=context)


def about(request):
    context = {
    }
    return render(request, template_name='blog/about.html', context=context)