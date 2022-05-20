from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    """ The home page that shows all First Blog post in chronological order."""
    posts = BlogPost.objects.filter(owner=request.user).order_by('date_added')
    context = {'posts': posts}
    return render(request, 'first_blog/index.html', context)

#def check_post_owner(request):
    # Make sure the post belongs to the current user.
    if BlogPost.owner != request.user:
        raise Http404
    else:
        return request
    
@login_required
def new_post(request):
    """Add a new post"""
    if request.method != 'POST':
        form = BlogPostForm
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('first_blog:index')
        
    context = {'form': form}
    return render(request, 'first_blog/new_post.html', context)

@login_required
def post(request, post_id):
    """Show a single post."""
    #check_post_owner(request)
    post = BlogPost.objects.get(id=post_id, owner=request.user)
    context = {'post': post}
    return render(request, 'first_blog/post.html', context)

@login_required
def edit_post(request, post_id):
    """Edit an existing post."""
    #check_post_owner(request)
    post = BlogPost.objects.get(id=post_id, owner=request.user)
    if request.method != 'POST':
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('first_blog:index')
    
    context = {'post': post, 'form': form}
    return render(request, 'first_blog/edit_post.html', context)
