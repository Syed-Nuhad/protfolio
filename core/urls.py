from django.urls import path
from . import views
from .views import contact_view

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
    path('contact/', contact_view, name='contact'),
]