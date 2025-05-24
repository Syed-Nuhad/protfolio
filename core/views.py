from django.shortcuts import render, get_object_or_404
from .models import About, Experience, Skill, Project, Review, NavbarLink, NavbarBrand, FooterInfo


def home(request):
    navbar_links = NavbarLink.objects.all()
    navbar_brand = NavbarBrand.objects.first()
    footer_info = FooterInfo.objects.first()
    context = {
        'footer_info': footer_info,
        'about': About.objects.first(),
        'experiences': Experience.objects.all(),
        'skills': Skill.objects.all(),
        'projects': Project.objects.all(),
        'navbar_links': navbar_links,
        'navbar_brand': navbar_brand,
    }
    return render(request, 'core/index.html', context)

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    reviews = project.reviews.all()
    context = {
        'project': project,
        'reviews': reviews,
    }
    return render(request, 'project_detail.html', context)
