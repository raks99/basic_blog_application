from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)  # A character field for the post title
    content = models.TextField()  # A text field for the post content.
    created_at = models.DateTimeField(default=timezone.now, editable=False)  # Editable is false, bcs this cannot be editable
    updated_at = models.DateTimeField(auto_now=True)  # automatically updates the date and time when a post is edited.

    def __str__(self):  # method is used to represent the Post objects as strings, typically in the admin interface. if anyone prints that out
        return self.title
    
