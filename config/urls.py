from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blog import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('blog.urls')),
    # Registration
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', views.site_logout, name='site_logout'),
    path('ask_login/', views.ask_login, name='ask_login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='site_logout'),
    path('profile/', views.profile, name='profile'),
    path('change/', views.change_profile, name='change_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
