"""Verzeo_Final_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('about/', include('home.urls')),
    path('project/', include('home.urls')),
    path('publication/',include('home.urls')),
    path('contact/', include('home.urls')),
    path('whitebrickhome/',include('home.urls')),
    path('XSECELTIC/',include('home.urls')),
    path('nordic/',include('home.urls')),
    path('classic/',include('home.urls')),
    path('kitchenpu/', include('home.urls')),
    path('composition/', include('home.urls')),
    path('natural/',include('home.urls')),
    path('kitchen/',include('home.urls')),
    path('minimalist/',include('home.urls')),
    path('mixing/',include('home.urls')),
    path('modelrust/',include('home.urls')),
    path('bluish/', include('home.urls')),
    path('XSapartments/', include('home.urls')),
    path('whitewonwhite/',include('home.urls')),
]
