from django.urls import path
from . import views
from .views import About

urlpatterns = [
    path('home/', views.home, name="home"),
    path('not_found', views.not_found, name="not_found"),
    path('about', About.as_view(), name="about"),
]