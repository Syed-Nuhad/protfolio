from django.shortcuts import render, get_object_or_404
from .models import Project

def index(request):
    projects = Project.objects.all()
    return render(request, 'core/index.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'core/project_detail.html', {'project': project})
