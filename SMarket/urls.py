from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ServedMView
from . import views

app_name="ServedMarket"
urlpatterns=[
    path('',views.ServedMView,name='ServedM'),
    path('OilGas',views.OilGasView,name='OilGas'),
    path('Offshore',views.OffshoreView,name='Offshore'),
    path('Onshore',views.OnshoreView,name='Onshore'),
    path('Pipe',views.PipeView,name='Pipe'),
    path('Energy',views.EnergyView,name='Energy'),
    path('Water&WasteWater',views.WaterView,name='Water'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)