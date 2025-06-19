from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('<int:blog_id>/view', views.detail, name='detail'),
]
