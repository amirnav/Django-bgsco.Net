from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import HomeView,AboutUsView,CertificateView

app_name="home"
urlpatterns=[
    path('',HomeView.as_view(),name='home'),
    path('aboutUs',AboutUsView.as_view(),name='aboutUs'),
    path('certificates',CertificateView.as_view(),name='certificates'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)