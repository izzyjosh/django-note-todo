from django.db import models
from django.contrib.auth.models import User


class Category(models.model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    category = models.CharField(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
