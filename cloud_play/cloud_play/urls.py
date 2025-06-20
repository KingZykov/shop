"""
URL configuration for cloud_play project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import index, profile_view, logout_view 
from . import views


urlpatterns = [
    path('', index, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('store/', views.store, name='store'),
    path('admin/', admin.site.urls),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('monitoring/', views.monitoring_users, name='monitoring_users'),
]
