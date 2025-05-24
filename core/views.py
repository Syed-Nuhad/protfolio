from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from .models import About, Experience, Skill, Project, Review, NavbarLink, NavbarBrand, FooterInfo, ContactSetting


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
def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        subject = f"New message from {name}"
        body = f"From: {name} <{email}>\n\nMessage:\n{message}"

        contact_setting = ContactSetting.objects.first()
        receiver = contact_setting.email_receiver if contact_setting else 'default@example.com'

        send_mail(
            subject,
            body,
            email,  # from
            [receiver],
            fail_silently=False
        )

        messages.success(request, 'Your message has been sent!')
        return redirect('home')  # or wherever your homepage is

    return redirect('home')
