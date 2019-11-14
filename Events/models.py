from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse 
from datetime import datetime

MAX_LENGTH_EVENT_NAME = 255
MAX_LENGTH_EVENT_DESCRIPTION = 1000


class Event(models.Model):
  eventId = models.AutoField(primary_key=True) 
  eventName = models.CharField(max_length = MAX_LENGTH_EVENT_NAME)
  eventDescription = models.CharField(max_length = MAX_LENGTH_EVENT_DESCRIPTION)
  eventDate = models.DateField()
  eventDatetime = models.DateTimeField()

  def __str__(self):
    return self.eventName
  
