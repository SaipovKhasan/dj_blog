from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from blog.forms import BlogForms, UserForms, CustomUserCreationForm, ProfileForm, CustomUserChangeForm
from blog.models import Blog, CustomUser, Profile
from django.contrib.auth import logout


@login_required
def home(request):
    blogs = Blog.objects.filter(is_active=True)
    search = request.GET.get('active_query')
    if search:
        blogs = Blog.objects.filter(title__icontains=search, is_active=True)
    context = {
        "blogs": blogs
    }
    return render(request, template_name='blog/home.html', context=context)


@login_required
def my_active_blogs(request):
    blog = Blog.objects.filter(is_active=True, author=request.user)

    search = request.GET.get('my_active_query')
    if search:
        blog = Blog.objects.filter(title__icontains=search, is_active=False, author=request.user)

    context = {
        "blogs": blog
    }
    return render(request, template_name='blog/my_blogs.html', context=context)


@login_required
def in_active(request):
    blog = Blog.objects.filter(is_active=False, author=request.user)

    search = request.GET.get('in_active_query')
    if search:
        blog = Blog.objects.filter(title__icontains=search, is_active=False, author=request.user)

    context = {
        "blogs": blog
    }
    return render(request, template_name='blog/in_active.html', context=context)


def about(request):
    context = {
    }
    return render(request, template_name='blog/about.html', context=context)


def detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    context = {
        "blog": blog
    }
    return render(request, template_name='blog/detail.html', context=context)


def update(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = BlogForms(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, message=f"{blog.title} updated successfully!")
            if blog.is_active:
                return redirect('home')
            else:
                return redirect('in_active_blogs')
    else:
        form = BlogForms(instance=blog)
    context = {
        "form": form,
        "blog": blog
    }
    return render(request, 'blog/update.html', context=context)


def delete(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('home')


def create(request):
    if request.method == 'POST':
        form = BlogForms(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()  # commit=True
            messages.success(request, message=f"{blog.title} created successfully")
            return redirect('home')
    else:
        messages.warning(request, message=f"We are currently in test mode!")
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
            messages.success(request, message=f'{user.username} username is created')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'blog/register.html', context=context)


def site_logout(request):
    logout(request)
    return redirect('ask_login')


def ask_login(request):
    return render(request, 'blog/logout.html')


def profile(request):
    user = get_object_or_404(CustomUser, id=request.user.id)
    profile = Profile.objects.filter(user__id=request.user.id).first()
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
        if u_form.is_valid():
            u_form.save()
        if p_form.is_valid():
            p_form.save()
        return redirect('profile', user.id)
    else:
        u_form = CustomUserChangeForm(instance=user)
        p_form = ProfileForm(instance=profile)

    context = {
        "u_form": u_form,
        "p_form": p_form
    }
    return render(request, 'user/profile_change.html', context=context)
