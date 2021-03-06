from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from app import views


urlpatterns = [
    path('admin', admin.site.urls), 
    path('login', views.login),
    path('register', views.register),
    path('news', views.news)
]
