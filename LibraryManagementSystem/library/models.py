# library/models.py

from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    description = models.TextField()
    ISBN = models.CharField(max_length=255, blank=True, null=True)
    Genre = models.CharField(max_length=255, blank=True, null=True)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField()
    image = models.ImageField(upload_to='authors/', blank=True, null=True)

class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(blank=True, null=True)
