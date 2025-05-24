from django.shortcuts import render, get_object_or_404
from .models import About, Experience, Skill, Project, Review

def home(request):
    context = {
        'about': About.objects.first(),
        'experiences': Experience.objects.all(),
        'skills': Skill.objects.all(),
        'projects': Project.objects.all(),
    }
    return render(request, 'core/home.html', context)

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    reviews = project.review_set.all()
    avg_rating = project.average_rating()
    context = {
        'project': project,
        'reviews': reviews,
        'avg_rating': avg_rating
    }
    return render(request, 'core/project_detail.html', context)
