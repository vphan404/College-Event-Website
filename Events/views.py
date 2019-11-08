from django.shortcuts import render

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

def home(request):

  context = {
    'posts': dummyPosts
  }

  return render(request, 'events/home.html', context)


def about(request):
  return render(request, 'events/about.html')
