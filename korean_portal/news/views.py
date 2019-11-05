from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Главная'
    }

    return render(request, 'news/home.html', context)


def about(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'О нас'
    }

    return render(request, 'news/about.html', context)
