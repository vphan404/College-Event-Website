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
  Rso
)
# from .forms import (
#   CreateRsoForm
# )

# Create your views here.


# Homepage
# def home(request):

#   context = {
#     'posts': dummyPosts
#     # 'events': Event.objects.all()
#   }

#   return render(request, 'events/home.html', context)


# Page that displays all the events
class RsoListView(ListView):
  model = Rso

  # Template = the html template 
  template_name = 'rso/rso_list.html'  # Default = <app>/<model>_<viewtype>.html
  
  # This is the info passed into the html
  context_object_name = 'rsos'

  # Orders in descending order by date (make the newest)
  # ordering = ['-date']


# # Page that displays the details for a given event
# class EventDetailView(DetailView):
#   model = Event 

#   template_name = 'events/event_detail.html'

#   def get_context_data(self, **kwargs):
#     # Call the base implementation first to get a context
#     context = super().get_context_data(**kwargs)

#     return context


# # Page for creating an event
# # class EventCreateView(CreateView):
# #   model = Event
# #   fields = [
# #     'name', 
# #     'description',
# #     'datetime'
# #   ]

# def EventCreateView(request):
#   model = Event
#   form = CreateEventForm(request.POST or None, request.FILES or None)
#   if request.method == 'POST' and form.is_valid():
#     form.save() 
#   context = {
#     'form': form,
#     'page_title': 'Edit Event',
#   }
#   return render(request, 'events/event_form.html', context)