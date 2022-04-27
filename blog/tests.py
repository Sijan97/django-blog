from cgi import test
from turtle import title
from urllib import response
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


class BlogTests(TestCase):
    """ Test cases for blog post model. """

    # Function that sets up demo post data for testing.
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@mail.com',
            password='testpass'
        )

        self.post = Post.objects.create(
            author=self.user,
            title='A good title',
            body='A good content'
        )

    # Function to test string representation.
    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    # Function to test post content.
    def test_post_content(self):
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.body}', 'A good content')

    # Function to test blog post list view.
    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A good content')
        self.assertTemplateUsed(response, 'home.html')

    # Function to test blog detail view.
    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/1000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')
