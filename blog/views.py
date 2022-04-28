from dataclasses import fields
from pyexpat import model
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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


class UpdatePostView(UpdateView):
    """ View definition to update/modify post. """
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class DeletePostView(DeleteView):
    """ View definition to delete post. """
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
