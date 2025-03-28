from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE
        )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['author', 'post']

    def __str__(self):
        return f"{self.author} {self.post}"
