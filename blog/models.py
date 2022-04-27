from tkinter import CASCADE
from django.db import models


class Post(models.Model):
    """ Database model definition for blog post. """
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()

    # Function that returns string representation of model.
    def __str__(self) -> str:
        return self.title
