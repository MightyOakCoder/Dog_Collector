from django.shortcuts import render

# Add the Dog class & list and view function below the imports
class Dog:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Walter', 'Domestic Short Hair', 'My son.', 8),
  Dog('Jack', 'Domestic Short Hair', 'Walter\'s bro.', 8),
  Dog('Clive', 'Tabby', 'Good guy. Sad story. Feels like you\'re petting a bag of bones.', 4)
]

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
    return HttpResponse('<h1>Home</h1>')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', { 'dogs': dogs })