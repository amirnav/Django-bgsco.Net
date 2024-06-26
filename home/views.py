from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse

from home.models import Participants


class HomeView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_url'] = reverse('home:home')  # Example URL, replace with your actual URL
        return context

class AboutUsView(TemplateView):
    template_name = "home/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_url'] = reverse('home:aboutUs')  # Example URL, replace with your actual URL
        return context

class CertificateView(TemplateView):
    template_name = "home/certificates.html"

def participantsView(request):
    participants=Participants.objects.all()
    return render(request,"home/index.html",{"participants":participants})

# Create your views here.
