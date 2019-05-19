from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# 文章栏目
class ArticleColumn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article_column')
    column = models.CharField(max_length=128)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column
