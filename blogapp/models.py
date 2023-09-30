from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    presentsion = models.TextField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', null=True, blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return f'пост: {self.title}, текст: {self.text}, создан: {self.created_at}, теги: {self.tags}'


class Comments(models.Model):
    authors = models.CharField(max_length=255)
    comments = models.TextField()
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f'автор: {self.authors}, комментарий: {self.comments}'


class Backgraund(models.Model):
    image = models.ImageField(upload_to='images/')