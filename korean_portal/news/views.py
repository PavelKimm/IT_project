from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Main',
        'news_home': True
    }

    return render(request, 'news/home.html', context)


def about(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'About Us',
        'news_about': True
    }

    return render(request, 'news/about.html', context)
