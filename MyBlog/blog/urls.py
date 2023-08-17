from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # List all posts
    path('', views.PostListView.as_view(), name='post_list'),

    # View a single post's details
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),

    # Create a new post
    path('create/', views.PostCreateView.as_view(), name='post_create'),

    # Edit an existing post
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),

    # Delete a post
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    
    # Search a post
    path('search/', views.PostSearchView.as_view(), name='post_search'),
]
