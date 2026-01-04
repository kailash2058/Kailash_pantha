# portfolio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #root url for my page
    path('contact/', views.contact_view, name='contact'),  # This line sets the URL for the contact view
    path('success/', views.success_view, name='success'),  # New success URL
    path('projects/', views.projects_all, name='projects_all'),  # Full projects listing
    path('blogs/', views.blogs_all, name='blogs_all'),  # Full blogs listing
    path('events/', views.events_all, name='events_all'),  # Full events listing
]