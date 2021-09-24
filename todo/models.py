from django.db import models

class Todo(models.Model):
    text = models.CharField(unique=True, max_length=300)

    def __str__(self):
        return self.text


