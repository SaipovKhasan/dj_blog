from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    # User registration
    path('register/', blog_views.register, name='register'),

    # User login, logout, profile
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', blog_views.site_logout, name='site_logout'),
    path('ask_login/', blog_views.ask_login, name='ask_login'),
    path('profile/', blog_views.profile, name='profile'),
    path('change/', blog_views.change_profile, name='change_profile'),

    # User Password Reset
    path('password/', auth_views.PasswordResetView.as_view(
        template_name='mail/password-reset.html'),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='mail/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='mail/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complated/', auth_views.PasswordResetCompleteView.as_view(
        template_name='mail/password_reset_complete.html'),
         name='password_reset_complete')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)