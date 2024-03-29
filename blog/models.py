from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class BlogArticles(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title
