from django import views
from django.contrib import admin
from django.urls import path
from introduceapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('favorite/', views.favorite, name='favorite'),
    path('photo/', views.photo, name='photo'),

    path('newguest/', views.newguest, name='newguest'),
]
