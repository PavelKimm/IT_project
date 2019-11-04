from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='news-home'),
    path('about/', views.about, name='news-about'),
]
