from django.db import models

class Status(models.Model):
    status_text = models.CharField(max_length = 200)
    def __str__(self):
        return self.status_text
class TodoItem(models.Model):
    todo_text = models.CharField(max_length=200)
    todo_status = models.ForeignKey(Status,on_delete=models.CASCADE)
    def __str__(self):
        return self.todo_text
