"""college_event_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from Users import views as user_views
from django.conf import settings # For images
from django.conf.urls.static import static # For images

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('Events.urls')),
    path('', include('Home.urls')),
    path('register/', include('Users.urls')),
    path('profile/', user_views.profile, name='profile'),
    re_path('profile/(?P<pk>\d+)/', user_views.profile, name='profile_with_pk'),
    path('edit_profile/', user_views.edit_profile, name='edit-profile'),
    path('rso/', include('Rso.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='Users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Users/logout.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
