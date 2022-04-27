from dataclasses import fields
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post


class BlogListView(ListView):
    """ List view definition for blog posts. """
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    """ Detail view for each blog posts. """
    model = Post
    template_name = 'post_detail.html'


class CreatePostView(CreateView):
    """ View definition to create new post. """
    model = Post
    template_name = 'post_new.html'
    fields = ['author', 'title', 'body']
