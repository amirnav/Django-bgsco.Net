from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import hiringView
from . import views

app_name="Hiring"
urlpatterns=[
    path('',views.hiringView,name='Hiring'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)