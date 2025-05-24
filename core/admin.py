from django.contrib import admin
from .models import About, Experience, Skill, Project, Review, NavbarBrand, NavbarLink, FooterInfo

admin.site.register(About)
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'duration']
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['project', 'user', 'rating', 'created_at']
admin.site.register(Review)
admin.site.register(NavbarLink)
admin.site.register(NavbarBrand)
admin.site.register(FooterInfo)