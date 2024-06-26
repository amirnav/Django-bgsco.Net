from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Project


def projectView(request):
    project=Project.objects.all()
    return render(request,"projects/projects.html",{"project":project})