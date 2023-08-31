from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.core.paginator import Paginator
from .models import Post
from django.urls import reverse_lazy
from rest_framework import generics
from .serializers import PostSerializer

# Create your views here.
class PostListView(ListView):  # it inherits from ListView class
    # ListView places the objects from the database in a context variable named object_list
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 12  # Implement pagination in the list view to display a limited number of posts per page.

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

# Adding search functionality
class PostSearchView(ListView):
    model = Post
    template_name = 'blog/post_search_results.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')  # Get the search query from the URL parameter
        if query:
            return Post.objects.filter(title__icontains=query)
        return Post.objects.none()  # Return an empty queryset if no search query is provided

# REST API view
class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    