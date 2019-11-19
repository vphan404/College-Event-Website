from django.urls import path
from .views import (
  EventListView
)
from . import views   # '.' = current directory

urlpatterns = [
  path('', 
    views.home, name='events-home'),

  path('test/', 
    EventListView.as_view(), name='event-list'),

  path('about/', 
    views.about, name='events-about')
]

