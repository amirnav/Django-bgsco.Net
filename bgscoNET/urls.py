from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('activities',include('activities.urls')),
    path('served',include('SMarket.urls')),
    path('projects',include('projects.urls')),
    path('career',include('career.urls')),
    path('contactUs',include('contactus.urls')),
]
