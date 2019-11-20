from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse 
from datetime import datetime, date, time

MAX_LENGTH_RSO_NAME = 255

def defaultUser():
  default = User.objects.first()
  if default is None:
    default = User.objects.create_user('defaultUser', password='djangoproject', last_login=DEFAULT_DATETIME)
  return default

def defaultRso():
  default = Rso.objects.first()
  if default is None:
    default = Rso(
      name = 'First Rso of Defaultness',
      description = 'A default Rso, filled to the brim with default-ness.',
    )
    default.save()
  # Returns the primary key, not the event itself
  return default.rsoId


class Rso(models.Model):
  id = models.AutoField(primary_key=True) 
  name = models.CharField(max_length = MAX_LENGTH_RSO_NAME)
  description = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE, default=defaultUser, null=True, blank=True)


  # This method returns a astring that represents this fclass.
  # similar to toString() in java
  def __str__(self):
    return self.name
  
  # Should associate a user with the event when initialized
  def save_model(self, request, obj, form, change):
    if obj.user == defaultUser:
      # Only set user during the first save.
      obj.user = request.user 
  
  # When you create/update an event, this is where the
  # page goes to after you save the event
  def get_absolute_url(self):
    return reverse('event-detail', kwargs={'pk:': self.pk})

