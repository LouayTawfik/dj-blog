from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from blog.forms import PostForm
from blog.models import Post


class post_list(ListView):
    model = Post

# def post_list(request):
#     data = Post.objects.all()
#     return render(request, 'blog/post_list.html', {'data': data})

class post_detail(DetailView):
    model = Post



# def post_detail(request, post_id):
#     post = Post.objects.get(pk=post_id)
#     return render(request, 'blog/post_detail.html', {'post': post})


class post_create(CreateView):
    model = Post
    fields = "__all__"
    success_url = "/post/list"

# def post_create(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             my_form = form.save(commit=False)
#             my_form.author = request.user
#             my_form.save()
#             return redirect('/post/list')
#     else:
#         form = PostForm()
#     return render(request, 'post_create.html', {'form': form})


# class PostCreate(CreateView):
#     model = Post
#     fields = ['title', 'content', 'image', 'tags', 'create_date', 'draft', 'author']
#     success_url = '/blog'



class post_update(UpdateView):
    model = Post
    fields = "__all__"
    success_url = "/post/list"
    template_name = "blog/post_update.html"



# def post_update(request, post_id):
#     post = Post.objects.get(pk=post_id)
#     if request.method == 'POST':
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'post_update.html', {'form': form})


class post_delete(DeleteView):
    model = Post
    success_url = "/post/list"


# def post_delete(request, post_id):
#     post = Post.objects.get(pk=post_id)
#     post.delete()