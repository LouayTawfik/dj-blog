from django.shortcuts import render, redirect

from blog.forms import PostForm
from blog.models import Post

def post_list(request):
    data = Post.objects.all()
    return render(request, 'post_list.html', {'data': data})

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})

def post_update(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
    else:
        form = PostForm(instance=post)
    return render(request, 'post_update.html', {'form': form})

def post_delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()