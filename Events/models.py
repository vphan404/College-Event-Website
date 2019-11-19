from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse 
from datetime import datetime

MAX_LENGTH_EVENT_NAME = 255
# MAX_LENGTH_EVENT_DESCRIPTION = 5000


def defaultUser():
  default = User.objects.first()

  if default is None:
    default = User.objects.create_user('defaultUser', password='djangoproject', last_login=DEFAULT_DATETIME)
  
  return default

def defaultEvent():
  default = Event.objects.first()

  if default is None:
    default = Event(
      eventName = 'First Event of Defaultness',
      eventDescription = 'A default event, filled to the brim with default-ness.',
      # eventDate = 
      # eventDatetime = 
    )
    default.save()
  
  # Returns the primary key, not the event itself
  return default.eventId




class Event(models.Model):
  eventId = models.AutoField(primary_key=True) 
  eventName = models.CharField(max_length = MAX_LENGTH_EVENT_NAME)
  eventDescription = models.TextField()
  eventDate = models.DateField()
  eventDatetime = models.DateTimeField()
  eventTime = models.TimeField()

  user = models.ForeignKey(User, on_delete=models.CASCADE, defualt=defaultUser, null=True, blank=True)


  # This method returns a astring that represents this fclass.
  # similar to toString() in java
  def __str__(self):
    return self.eventName
  
  # Should associate a user with the event when initialized
  def save_model(self, request, obj, form, change):
    if obj.user == defaultUser:
      # Only set user during the first save.
      obj.user = request.user 
  
  # When you create/update an event, this is where the
  # page goes to after you save the event
  def get_absolute_url(self):
    return reverse('event-detail', kwargs={'pk:': self.pk})

