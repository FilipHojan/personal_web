from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=140)
    body = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_publish = models.DateTimeField(blank=True, null=True)
    public = models.BooleanField(default=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title