from django.db import models

# Create your models here.


class Site(models.Model):
    url = models.CharField(max_length=1000)
    speed_index = models.CharField(max_length=50)
    time_to_interactive = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
