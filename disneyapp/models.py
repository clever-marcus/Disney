from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
CATEGORY_CHOICES = (
    ('A', 'ACTION'),
    ('D', 'DRAMA'),
    ('C', 'COMEDY'),
    ('R', 'ROMANCE'),
)

AGE_CHOICES = (
    ('all', 'All'),
    ('seasonal', 'Seasonal')
)

LANGUAGE_CHOICES = (
    ('EN', 'ENGLISH'),
    ('FR', 'FRENCH'),
)



class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='static/images')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2)

    def __str__(self):
        return self.title

