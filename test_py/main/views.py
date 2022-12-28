
from django.shortcuts import render
from django.views import generic
from .models import Car
class CarListView(generic.ListView):
    queryset = Car.objects.all()
    template_name = 'static/carlist.html'
    context_objects_name = 'car'
class CarDetailView(generic.DetailView):
    model = Car
    template_name='static/cardetail.html'
    context_objects_name='car'