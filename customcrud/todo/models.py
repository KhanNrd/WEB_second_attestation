from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=100)
    isDone = models.BooleanField(default=False)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'isDone': self.isDone,
        }
