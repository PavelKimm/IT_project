from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    post_detail)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='news-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', post_detail, name='post-detail'),
    # path('post/<int:pk>/add_comment/', CommentCreateView.as_view(), name='add-comment'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='news-about'),
]
