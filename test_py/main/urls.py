
from django.urls import path
from django.shortcuts import render,HttpResponse
from .views import CarListView

def car(reguest):
    return HttpResponse('<div align="center"><h1 style="color:red">ads</h1></div>')
urlpatterns = [
    path('',CarListView.as_view(), name='car_list')
]
