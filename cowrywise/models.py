from django.db import models
from datetime import datetime

# Create your models here.

class TimeStamp(models.Model):

	
    timestamp = models.CharField(max_length=150)
    uuid = models.CharField(max_length=150)

    def __str__(self):
        return str(self.uuid)
