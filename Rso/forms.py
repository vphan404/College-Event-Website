from django import forms
from django.forms import TimeInput, DateInput
from .models import (
  Rso
)

# What should be listed on a create rso form
class CreateRsoForm(forms.ModelForm):
  class Meta:
    model = Rso 
    fields = [
      'name',
      'description',
      'members'
    ]