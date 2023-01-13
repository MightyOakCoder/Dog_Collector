from django.shortcuts import render
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