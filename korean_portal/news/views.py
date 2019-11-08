from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Main',
        'news_home': True
    }
    return render(request, 'news/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'news/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'About Us',
        'news_about': True
    }

    return render(request, 'news/about.html', context)
