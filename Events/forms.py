from django import forms
from .models import (
  Event
)

# What should be listed on a create event form
class CreateEventForm(forms.ModelForm):
  class Meta:
    model = Event 
    fields = [
      'eventName',
      'eventDescription',
      'eventDatetime'
    ]