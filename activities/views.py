from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class activitiesView(TemplateView):
    template_name ="activities/activities.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['activities'] = 'activities'
        return context

    def activityView(request):
        activities = activitiesView.as_view
        return render(request, "activities/activities.html", {"activities": activities})
# Create your views here.
def SCADA(request):
    return render(request,"activities/SCADA and automation.html")

def TELECom(request):
    return render(request,"activities/Telecommunication and Networking.html")

def IndDatCent(request):
    return render(request,"activities/Industrial Data Center.html")

def ProtectRelays(request):
    return render(request,"activities/ProtectiveRelays.html")


def PatiOverseas(request):
    return render(request,"activities/ParticipationOverseas.html")

def SupplyEquip(request):
    return render(request, "activities/Procurement.html")


