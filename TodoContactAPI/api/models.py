from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=300, blank=True)
    description = models.TextField()
    priority = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
     )
    #done = models.BooleanField(default=False)

def __str__(self):
    return self.title

class Contact(models.Model):
    name = models.CharField(max_length=300, blank=True)
    number = models.IntegerField(
        default=100,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    image = models.CharField(max_length=1000, blank=True)

def __str__(self):
    return self.name