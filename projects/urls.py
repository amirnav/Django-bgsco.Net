from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import projectView
from . import views

app_name="Project"
urlpatterns=[
    path('',views.projectView,name='Project'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)