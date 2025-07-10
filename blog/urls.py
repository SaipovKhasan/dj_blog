from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('about/', views.about, name='about'),
    path('in_actives/', views.in_active, name='in_active_blogs'),
    path('my_active_blogs/', views.my_active_blogs, name='my_active_blogs'),
    path('<int:blog_id>/view', views.detail, name='detail'),
    path('<int:blog_id>/update', views.update, name='update'),
    path('<int:blog_id>/delete', views.delete, name='delete'),
    path('test-email/', views.test_email, name='test_email')

]
