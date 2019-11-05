from django.shortcuts import render

posts = [
    {
        'author': 'Pavel',
        'title': 'News post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2019'
    },
    {
        'author': 'Roma',
        'title': 'News post 2',
        'content': 'Second post content',
        'date_posted': 'August 29, 2019'
    }
]

def home(request):
    context = {
        'posts': posts,
        'title': 'Главная'
    }

    return render(request, 'news/home.html', context)


def about(request):
    context = {
        'posts': posts,
        'title': 'О нас'
    }

    return render(request, 'news/about.html', context)
