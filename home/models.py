from django.db import models

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to="uploads/")
    is_liked = models.BooleanField(default=False)