from django.conf.urls.static import static
from django.urls import path, include
from bgscoNET import settings
from .views import activitiesView
from . import views

app_name="activities"
urlpatterns=[
    path("",activitiesView.as_view(),name="activities"),
    path("/SkadaAutomation",views.SCADA,name="Skada"),
    path("/Telecom",views.TELECom,name="TeleCom"),
    path("/IndustrialDataCenter",views.IndDatCent,name="IndDatCen"),
    path("/ProtectRelays",views.ProtectRelays,name="ProtectRel"),
    path("/Overseas",views.PatiOverseas,name="PartOverseas"),
    path("/Supply&Equip",views.SupplyEquip,name="Supply"),
]