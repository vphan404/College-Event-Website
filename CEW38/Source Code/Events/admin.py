from django.contrib import admin
from .models import Event, Comment

# Register your models here to show up on admin page
admin.site.register(Event)
admin.site.register(Comment)