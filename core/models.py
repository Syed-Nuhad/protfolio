from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# About Section
class About(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return "About Section"

# Experience Section
class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

# Skills Section
class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Project Section


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    live_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_url(self):
        return reverse('project_detail', args=[str(self.id)])

    def average_review(self):
        reviews = self.reviews.all()
        if not reviews:
            return 0
        return round(sum([r.rating for r in reviews]) / reviews.count(), 1)

    def review_count(self):
        return self.reviews.count()

    def __str__(self):
        return self.title

class Review(models.Model):
    project = models.ForeignKey(Project, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s review on {self.project.title}"

# Reviews
class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name}"

class NavbarLink(models.Model):
    name = models.CharField(max_length=50)
    target_id = models.CharField(max_length=50)  # e.g. 'intro', 'about', etc.
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


class NavbarBrand(models.Model):
    brand_name = models.CharField(max_length=100)

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = "Navbar Brand"
        verbose_name_plural = "Navbar Brand"

class FooterInfo(models.Model):
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Footer Info'
        verbose_name_plural = 'Footer Info'

    def __str__(self):
        return "Footer Info"