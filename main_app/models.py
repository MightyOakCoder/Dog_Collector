from django.db import models
from django.urls import reverse

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    favorite_activity = models.TextField(max_length=250)
    famous_for = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    # this makes it so it says the cat's name instead of just Cat object

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})