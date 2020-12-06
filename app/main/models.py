from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name
