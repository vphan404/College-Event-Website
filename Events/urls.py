from django.urls import path
from .views import (
  EventListView,
  EventDetailView
)
from . import views   # '.' = current directory

urlpatterns = [
  path('', 
    views.home, name='events-home'),

  path('test/', 
    EventListView.as_view(), name='event-list'),
  
  path('event/<int:pk>/',
    EventDetailView.as_view(), name='event-detail'),

  path('about/', 
    views.about, name='events-about')
]

