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
  Rso
)
from .forms import (
  CreateRsoForm
)

# Create your views here.

# Page that displays all the rso
class RsoListView(ListView):
  model = Rso

  # Template = the html template 
  template_name = 'rso/rso_list.html'  # Default = <app>/<model>_<viewtype>.html
  
  # This is the info passed into the html
  context_object_name = 'rsos'

  # Orders in descending order by date (make the newest)
  # ordering = ['-date']


# Page that displays the details for a given event
class RsoDetailView(DetailView):
  model = Rso 

  template_name = 'rso/rso_detail.html'

  def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
    context = super().get_context_data(**kwargs)

    return context

def RsoCreateView(request):
  model = Rso
  form = CreateRsoForm(request.POST or None, request.FILES or None)
  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('rso-home')
  context = {
    'form': form,
    'page_title': 'Edit Rso',
  }
  return render(request, 'rso/rso_form.html', context)