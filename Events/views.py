from django.shortcuts import render, redirect
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
  Event,
  Comment
)
from .forms import (
  CreateEventForm,
  CreateCommentForm
)

# Create your views here.


# Page that displays all the events
class EventListView(ListView):
  model = Event

  # Template = the html template 
  template_name = 'events/event_list.html'  # Default = <app>/<model>_<viewtype>.html
  
  # This is the info passed into the html
  context_object_name = 'events'

  # Orders in descending order by date (make the newest first)
  ordering = ['-date']


# Page that displays the details for a given event
class EventDetailView(DetailView):
  model = Event 

  template_name = 'events/event_detail.html'

  def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
    context = super().get_context_data(**kwargs)
    context['comments'] = Comment.objects.all()

    return context


# Page for creating an event
# class EventCreateView(CreateView):
#   model = Event
#   fields = [
#     'name', 
#     'description',
#     'datetime'
#   ]

def EventCreateView(request):
  model = Event
  form = CreateEventForm(request.POST or None, request.FILES or None)
  if request.method == 'POST' and form.is_valid():
    form.save() 
    return redirect('events-home')
  context = {
    'form': form,
    'page_title': 'Create Event',
  }
  return render(request, 'events/event_form.html', context)

def CommentCreateView(request):
  model = Comment
  form = CreateCommentForm(request.POST or None, request.FILES or None) 
  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('events-home') 
  context = {
    'form': form,
    'page_title': 'Create Comment' 
  }
  return render(request, 'events/comment_form.html', context)