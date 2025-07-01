from django.urls import path
from blog import views as blog_views

urlpatterns = [
    path('', blog_views.home, name='home'),
    path('create/', blog_views.create, name='create'),
    path('about/', blog_views.about, name='about'),
    path('in_actives/', blog_views.in_active, name='in_active_blogs'),
    path('my_active_blogs/', blog_views.my_active_blogs, name='my_active_blogs'),
    path('<int:blog_id>/view', blog_views.detail, name='detail'),
    path('<int:blog_id>/update', blog_views.update, name='update'),
    path('<int:blog_id>/delete', blog_views.delete, name='delete'),
]