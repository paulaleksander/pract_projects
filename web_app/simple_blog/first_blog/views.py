from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    """ The home page that shows all First Blog post in chronological order."""
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'first_blog/index.html', context)

def new_post(request):
    """Add a new post"""
    if request.method != 'POST':
        form = BlogPostForm
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('first_blog:index')
        
    context = {'form': form}
    return render(request, 'first_blog/new_post.html', context)

def edit_post(request, post_id):
    """Edit an existing post."""
    post = BlogPost.objects.get(id=post_id)
    
    if request.method != 'POST':
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('first_blog:index')
    
    context = {'post': post, 'form': form}
    return render(request, 'first_blog/edit_post.html', context)
