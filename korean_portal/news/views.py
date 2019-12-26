from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from news.forms import CommentForm
from .models import Post, Comment


class PostListView(ListView):
    model = Post
    template_name = 'news/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['news_home'] = True
        return context


class UserPostListView(ListView):
    model = Post
    template_name = 'news/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False


def post_detail(request, pk):
    posts = Post.objects.all()
    post = get_object_or_404(Post, id=pk)
    comments_list = Comment.objects.filter(post=post).order_by('-id')
    paginator = Paginator(comments_list, 3)

    page = request.GET.get('page')
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(post=post,
                                             sender=request.user,
                                             content=content)
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()

    context = {
        'posts': posts,
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'pk': pk,
        'object': post
    }
    return render(request, 'news/post_detail.html', context)


@login_required
def comment_delete(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user == comment.sender:
        Comment.objects.filter(id=comment_id).delete()
        return redirect('post-detail', pk=comment.post_id)


def about(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'About Us',
        'news_about': True
    }
    return render(request, 'news/about.html', context)


def contacts(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Contacts',
        'news_contacts': True
    }
    return render(request, 'news/contacts.html', context)


def history(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'History of the Koreans'
    }
    return render(request, 'news/history.html', context)


def cuisine(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Korean cuisine'
    }
    return render(request, 'news/cuisine.html', context)


def traditions(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Korean traditions'
    }
    return render(request, 'news/traditions.html', context)


def leisure(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Korean leisure'
    }
    return render(request, 'news/leisure.html', context)


def gallery(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Gallery'
    }
    return render(request, 'news/gallery.html', context)
