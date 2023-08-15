from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_posts = ['title', 'created_at', 'updated_at']
admin.site.register(Post)  # this will register


