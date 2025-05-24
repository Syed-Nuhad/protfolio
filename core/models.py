from django.db import models
from django.utils.text import slugify

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
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    live_link = models.URLField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def average_rating(self):
        reviews = self.review_set.all()
        if reviews.exists():
            return round(sum([r.rating for r in reviews]) / reviews.count(), 1)
        return 0

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

