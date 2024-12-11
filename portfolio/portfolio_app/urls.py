# portfolio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #root url for my page
    path('contact/', views.contact_view, name='contact'),  # This line sets the URL for the contact view
    path('success/', views.success_view, name='success'),  # New success URL

]