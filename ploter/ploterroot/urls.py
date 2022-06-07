from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
      path('', views.index,name='index'),
      path('polygon/',views.polygon,name="polygon"),
      path('/circle',views.circle,name="circle"),
    
]