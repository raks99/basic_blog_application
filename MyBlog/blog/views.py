from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


# Create your views here.
class PostListView(ListView):  # it inherits from ListView class
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  #
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'  #
    fields = ['title', 'content']  # 
    success_url = reverse_lazy('blog:post_list')  # class PostListView(ListView):  # it inherits from ListView class
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  #
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'  #
    fields = ['title', 'content']  # 
    success_url = reverse_lazy('blog:post_list')
    
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_form.html'  #
    fields = ['title', 'content']  # 
    success_url = reverse_lazy('blog:post_list')  # redirect him back to the list of all blog posts

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'  #
    success_url = reverse_lazy('blog:post_list')  # redirect him back to the list of all blog posts
    
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_form.html'  #
    fields = ['title', 'content']  # 
    success_url = reverse_lazy('blog:post_list')  # redirect him back to the list of all blog posts

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'  #
    success_url = reverse_lazy('blog:post_list')  # redirect him back to the list of all blog posts

