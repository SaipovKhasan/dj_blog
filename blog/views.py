import random
from dataclasses import dataclass

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import BlogForms, CustomUserCreationForm, ProfileForm, CustomUserChangeForm, CommentForm
from blog.models import Blog, CustomUser, Profile, Comment


@login_required
def home(request):
    blogs = Blog.objects.filter(is_active=True)

    search = request.GET.get('active_query')
    if search:
        blogs = Blog.objects.filter(title__icontains=search, is_active=True)

    paginator = Paginator(blogs, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "blog_count": paginator.count
    }
    return render(request, template_name='blog/home.html', context=context)


@login_required
def my_active_blogs(request):
    blogs = Blog.objects.filter(is_active=True, author=request.user)
    search = request.GET.get('my_active_query')
    if search:
        blogs = Blog.objects.filter(title__icontains=search, is_active=False, author=request.user)

    context = {
        "blogs": blogs,
    }
    return render(request, template_name='blog/my_blogs.html', context=context)


@login_required
def in_active(request):
    blogs = Blog.objects.filter(is_active=False, author=request.user)
    search = request.GET.get('in_active_query')
    if search:
        blogs = Blog.objects.filter(title__icontains=search, is_active=False, author=request.user)

    context = {
        "blogs": blogs,
    }
    return render(request, template_name='blog/in_active.html', context=context)


def about(request):
    context = {
    }
    return render(request, template_name='blog/about.html', context=context)


def detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comments = Comment.objects.filter(blog=blog)
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.blog = blog
        comment.save()
        return redirect('detail', blog_id=blog_id)
    context = {
        "blog": blog,
        "comment_form": comment_form,
        "comments": comments
    }
    return render(request, template_name='blog/detail.html', context=context)


def update(request, blog_id):
    if request.user.has_perm('blog.change_blog'):
        blog = get_object_or_404(Blog, id=blog_id)
    else:
        blog = get_object_or_404(Blog, id=blog_id, author=request.user)

    if request.method == 'POST':
        form = BlogForms(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save()
            messages.success(request, message=f"{blog.title} o'zgartirildi!")
            if blog.is_active:
                return redirect('home')
            return redirect('in_active_blogs')
    else:
        form = BlogForms(instance=blog)
    context = {
        "form": form,
        "blog": blog
    }
    return render(request, 'blog/update.html', context=context)


def delete(request, blog_id):
    if request.user.has_perm('blog.delete_blog'):
        blog = get_object_or_404(Blog, id=blog_id, author=request.user)
        blog.delete()
    else:
        return HttpResponse('Siz bu blogni ochira olmaysiz')
    return redirect('home')


def create(request):
    if request.method == 'POST':
        form = BlogForms(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()  # commit=True
            messages.success(request, message=f"{blog.title} yaratildi!")
            return redirect('home')
    else:
        messages.warning(request, message=f"Hozirda biz test rejimida ishlayapmiz!")
        form = BlogForms()

    context = {
        "form": form
    }
    return render(request, 'blog/create_blog.html', context=context)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, message=f"{user.username} username li foydalanuvchi yaratildi!")
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form
    }
    return render(request, 'blog/register.html', context=context)


def site_logout(request):
    logout(request)
    return redirect('ask_login')


def ask_login(request):
    return render(request, 'blog/ask_login.html')


def profile(request):
    user = get_object_or_404(CustomUser, id=request.user.id)
    profile = Profile.objects.filter(user__id=user.id).first()
    context = {
        "user": user,
        "profile": profile
    }
    return render(request, 'user/profile.html', context=context)


def change_profile(request):
    user = get_object_or_404(CustomUser, id=request.user.id)
    profile = Profile.objects.filter(user__id=request.user.id).first()
    if request.method == 'POST':
        u_form = CustomUserChangeForm(request.POST, instance=user)
        p_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            profile = p_form.save(commit=False)
            profile.user = request.user
            profile.save()

        return redirect('profile')
    else:
        u_form = CustomUserChangeForm(instance=user)
        p_form = ProfileForm(instance=profile)

    context = {
        "u_form": u_form,
        "p_form": p_form
    }
    return render(request, 'user/profile_change.html', context=context)


def test_email(request):
    send_mail(
        'Test',
        'Message test',
        'saipovxasan10@gmail.com',
        CustomUser.objects.values_list('email', flat=True),
        fail_silently=False,
    )
    return HttpResponse('Test email muvoffaqqiyatli yuborildi!')


