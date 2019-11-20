from django import forms
from django.forms import TimeInput, DateInput
from address.forms import AddressField
from .models import (
  Event
)

# What should be listed on a create event form
class CreateEventForm(forms.ModelForm):
  # address = AddressField()
  class Meta:
    model = Event 
    fields = [
      'name',
      'description',
      'date',
      'startTime',
      'endTime',
      # 'address'
      'location',
      'isPrivate',
      'isRSO'
    ]
    widgets = {
      'date': forms.SelectDateWidget(),
      'startTime': forms.TimeInput(),
      'endTime': forms.TimeInput()
    }
    # name = forms.CharField(max_length=)
    # date = forms.DateField(
    #   widget=forms.SelectDateWidget(years=[2001, 2002])
    # )