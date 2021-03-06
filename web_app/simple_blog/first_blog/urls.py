"""Defines URL patterns for first_blog."""
from django.urls import path
from . import views

app_name = 'first_blog'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page for create a new post.
    path('new_post/', views.new_post, name='new_post'),
    # Page for a post
    path('post/<int:post_id>/', views.post, name='post'),
    # Page for editing posts.
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]