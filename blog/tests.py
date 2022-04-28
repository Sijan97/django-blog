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

    # Function to test get_absolut_url.
    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    # Function to test create post view.
    def test_create_post_view(self):
        response = self.client.post(reverse('post_new'), {
            'author': self.user.id,
            'title': 'New title',
            'body': 'New body',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'New title')
        self.assertEqual(Post.objects.last().body, 'New body')

    # Function to test edit post view.
    def test_edit_post_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Updated title',
            'body': 'Updated body',
        })
        self.assertEqual(response.status_code, 302)

    # Function to test delete post view.
    def test_delete_post_view(self):
        response = self.client.post(reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 302)
