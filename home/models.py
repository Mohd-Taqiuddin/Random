from django.db import models
from django.db.models.fields import NullBooleanField

# Create your models here.

class Event(models.Model):
    email = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50, default="")
    event_name = models.CharField(max_length=50, default="")
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to="uploads/")
    is_liked = models.BooleanField(default=False)