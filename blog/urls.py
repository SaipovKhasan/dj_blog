from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('in_actives', views.in_active, name='in_active_blogs'),
    path('<int:blog_id>/view', views.detail, name='detail'),
    path('about/', views.about, name='about'),
    path('<int:blog_id>/update', views.update, name='update'),
    path('<int:blog_id>/delete', views.delete, name='delete'),
    path('create/', views.create, name='create'),
    # path('search/', views.search, name='search'),
]
