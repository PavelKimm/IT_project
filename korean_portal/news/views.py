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
    return render(request, 'news/home.html')

def about(request):
    context = {
        'posts': posts,
        'title': 'About'
    }
    return render(request, 'news/about.html', context)
