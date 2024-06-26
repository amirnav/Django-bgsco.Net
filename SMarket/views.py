from django.shortcuts import render
from django.views.generic import TemplateView


def ServedMView(request):
    return render(request,"SMarket/SMarket.html")
def OilGasView(request):
    return render(request,"SMarket/Oil&Gas.html")
def OffshoreView(request):
    return render(request,"SMarket/Offshore.html")
def OnshoreView(request):
    return render(request,"SMarket/Onshore.html")
def PipeView(request):
    return render(request,"SMarket/Oil Pipeline.html")
def EnergyView(request):
    return render(request,"SMarket/Energy.html")
def WaterView(request):
    return render(request,"SMarket/Water.html")