from django.db import models
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=35, default=None)
    videofile = models.FileField(upload_to='images/', null=True, verbose_name="", default=None)
    summary = models.CharField(max_length=255, default=None)
    created_at = models.DateTimeField(auto_now_add=True)



class PostMeta(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=255, default=None)


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=255)


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

