from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
    return HttpResponse('<h1>Home</h1>')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.order_by('name')
    return render(request, 'dogs/index.html', { 'dogs': dogs })

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/detail.html', { 'dog': dog })

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'
    success_url = '/dogs/'

class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'favorite_activity', 'famous_for']

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'