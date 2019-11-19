from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
  UpdateView,
  DeleteView
)

from .models import (
  Event
)
from .forms import (
  CreateEventForm
)

# Create your views here.

# Temporary dummy variable representing what a SQL query could return
dummyPosts = [
  {
    'author': 'Bobby Jackson',
    'title': 'Blog Post 1',
    'content': 'First post content goes here.',
    'date_posted': 'October 30, 2019'
  },
  {
    'author': 'James Sullivan III',
    'title': 'Blog Post 2',
    'content': "Second post content goes here. It's a pretty spoopy day today",
    'date_posted': 'October 31, 2019'
  },
]


dummyEvents = [
  {
    'eventName': 'My First Event',
    'eventDescription': 'Some description goes here, can be arbitrarily long',
    'eventDatetime': 'October 30, 2019'
  }, 
  {
    'eventName': 'Second Event',
    'eventDescription': 'Some other description goes here.',
    'eventDatetime': 'October 31, 2019'
  }
]

# Homepage
def home(request):

  context = {
    'posts': dummyPosts
    # 'events': Event.objects.all()
  }

  return render(request, 'events/home.html', context)

# Page that displays all the events
class EventListView(ListView):
  model = Event

  # Template = the html template 
  template_name = 'events/home.html'  # Default = <app>/<model>_<viewtype>.html
  
  
  context_object_name = 'events'


  ordering = ['-eventDateTime']



# About page.
def about(request):
  return render(request, 'events/about.html')
