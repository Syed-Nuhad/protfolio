from django.contrib import admin
from .models import About, Experience, Skill, Project, Review

admin.site.register(About)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Review)