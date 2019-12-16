from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    post_detail,
    comment_delete)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='news-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', post_detail, name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('comment/<int:comment_id>/delete', comment_delete, name='comment-delete'),

    path('about/', views.about, name='news-about'),
    path('contacts/', views.contacts, name='news-contacts'),
    path('history/', views.history, name='news-history'),
    path('cuisine/', views.cuisine, name='news-cuisine'),
    path('traditions/', views.traditions, name='news-traditions'),
    path('leisure/', views.leisure, name='news-leisure'),
    path('gallery/', views.gallery, name='news-gallery'),
]
