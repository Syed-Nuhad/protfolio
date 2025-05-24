from django.contrib import admin
from .models import About, Experience, Skill, Project, Review
from .models import Experience


admin.site.register(About)
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'duration']
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Review)