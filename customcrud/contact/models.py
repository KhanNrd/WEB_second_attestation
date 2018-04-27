from django.db import models


# Create your models here.
class Contact(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=20)

    class Meta:
        ordering = ('created',)
