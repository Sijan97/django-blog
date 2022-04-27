from pyexpat import model
from re import template
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class BlogListView(ListView):
    """ List view definition for blog posts. """
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    """ Detail view for each blog posts. """
    model = Post
    template_name = 'post_detail.html'
