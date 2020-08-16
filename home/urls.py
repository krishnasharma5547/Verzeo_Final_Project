from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('project/', views.project, name = 'project'),
    path('publication/', views.publication, name = 'publication'),
    path('contact/', views.contact, name = 'contact'),
    path('whitebrickhome/', views.whitebrickhome, name="whitebrickhome"),
    path('XSECELTIC/', views.XSECELTIC, name='XSECELTIC'),
    path('nordic/', views.nordic, name='nordic'),
    path('classic/', views.classic, name='classic'),
    path('kitchenpu/', views.kitchenpu, name="kitchenpu"),
    path('composition/', views.composition, name="composition"),
    path('natural/',views.natural, name="natural"),
    path('kitchen/',views.kitchen, name="kitchen"),
    path('minimalist/', views.minimalist, name="minimalist"),
    path('mixing/', views.mixing, name = "mixing"),
    path('modelrust/', views.modelrust, name = "modelrust"),
    path('bluish/', views.bluish, name="bluish"),
    path('XSapartments/', views.XSapartments, name="XSapartments"),
    path('whitewonwhite/', views.whitwonwhite, name='whitwonwhite'),
]
