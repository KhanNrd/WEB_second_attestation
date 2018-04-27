from django.db import models

class Person(models.Model):
    person_name = models.CharField(max_length = 200)
    person_phone = models.CharField(max_length = 200)
    person_photo = models.ImageField(upload_to='contact/photo/',
                             blank=True)
