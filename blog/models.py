from django.db import models
from django.urls import reverse


class Post(models.Model):
    """ Database model definition for blog post. """
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()

    # Function that returns string representation of model.
    def __str__(self) -> str:
        return self.title

    # Function to set cannonical url.
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
