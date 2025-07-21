from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name #<Post object at address0x7f8e1a3b5d30> if self use then Post.name in str
    


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField("Category", related_name="posts")
    is_published = models.BooleanField(default=True)  # <-- Add this field
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
    class Meta:
        ordering = ['-created_on']

#S16q^960
