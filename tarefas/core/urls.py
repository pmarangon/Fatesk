 
from django.contrib import admin
from django.urls import path,include
from .import  views
from core.views import agenda
app_name = 'core'


urlpatterns = [
   path('agenda', views.agenda),
   path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('pendentes', views.pendentes)
    
]

 
