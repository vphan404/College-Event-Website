from django.db import models
# from django.contrib.auth.models import User 
from django.urls import reverse 
from datetime import datetime, date, time

# from django.contrib.gis.db import models
# from django.contrib.gis.geos import Point
# from location_field.models.spatial import LocationField # For the location widget
from location_field.models.plain import PlainLocationField

from address.models import AddressField, Address

from Users.models import User
from Universities.models import University, defaultUniversity

MAX_LENGTH_EVENT_NAME = 255
DEFAULT_DATE = date(2000, 1, 1)
DEFAULT_START_TIME = time(12, 0)
DEFAULT_END_TIME = time(13, 0)
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
      name = 'First Event of Defaultness',
      description = 'A default event, filled to the brim with default-ness.',
      date = date(2015, 1, 1),
      startTime = time(12, 30),
      endTime = time(13, 30)
    )
    default.save()
  
  # Returns the primary key, not the event itself
  return default.eventId

def defaultLocation():
  default = '28.6024, -81.2001' # UCF
  return default

def defaultAddress():
  rawText = '4000 Central Florida Blvd, Orlando, FL 32816'
  default = Address.objects.first() 

  if default is None:
    default = Address.objects.create(
      raw = '4000 Central Florida Blvd, Orlando, FL 32816'
    )
  # dictionary = {
  #   'raw':rawText
  # }
  # default = Address(
  #   dictionary
  # )
  # default = Address( 
  #   'defaultAddress',
  #   raw='4000 Central Florida Blvd, Orlando, FL 32816',
  #   street_number=4000,
  # )
  # default = Address(rawText)
  # default = '4000 Central Florida Blvd, Orlando, FL 32816'
  return default



class Event(models.Model):
  id = models.AutoField(primary_key=True) 
  name = models.CharField(max_length = MAX_LENGTH_EVENT_NAME)
  description = models.TextField()
  date = models.DateField(default=DEFAULT_DATE)
  startTime = models.TimeField(default=DEFAULT_START_TIME)
  endTime = models.TimeField(default=DEFAULT_END_TIME)
  location = PlainLocationField(based_fields=['city'], zoom=7, default=defaultLocation())
  isApproved = models.BooleanField(default=False)
  isPrivate = models.BooleanField(default=False) 
  isRSO = models.BooleanField(default=False)
  # university = models.ForeignKey(University, default=defaultUniversity(), on_delete=models.CASCADE)
  # address = AddressField(null=True, on_delete=models.CASCADE)
  # University
  # begin time, end time?

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


class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField(default='Type your comment here!')
  event = models.ForeignKey(Event, on_delete=models.CASCADE) 

  def save_model(self, request, obj, form, change):
    if obj.user == defaultUser: 
      obj.user = request.user 
  
  def __str__(self):
    return f'{self.event.name} {self.user.username}'