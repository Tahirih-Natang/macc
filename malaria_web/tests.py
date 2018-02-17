from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from .forms import *
from .views import *
from .urls import *
import json

class Setup_Class(TestCase):

    def setUp(self):
        self.post = Post.objects.create(title_post="post", description_post="Description", link_post="url", photo="image")

class Post_Form_Test(TestCase):

    # Valid Form Data
    def test_PostForm_valid(self):
        form = PostForm(data={'title_post': "post", 'description_post': "Description", 'link_post': "url", 'photo': "image"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_PostForm_invalid(self):
        form = PostForm(data={'title_post': "", 'description_post': "mp", 'link_post': "mp", 'photo': ""})
        self.assertFalse(form.is_valid())

class View_Test(TestCase)
    def setUp(self):
        self.factory = RequestFactory()
        with open('credentials.json') as json_data:
            credentials = json.load(json_data)
        self.user = User.objects.create_user(username=credentials['user'], email='tahir@…', password=credentials['password'])

    def test_list_posts_view(self):
        request = self.factory.get('/list_posts/')
        request.user = self.user
        response = ListPostView.as_view()(request)
        self.assertTemplateUsed("malaria/list_posts.html")
        self.assertEqual(response.status_code, 200)

    def test_create_posts_view(self):
        request = self.factory.get('/create_post/')
        request.user = self.user
        response = CreatePostView.as_view()(request)
        self.assertTemplateUsed("malaria/create_post.html")
        self.assertEqual(response.status_code, 200)

    def test_update_posts_view(self):
        request = self.factory.get('/edit_post/')
        request.user = self.user
        response = UpdatePostView.as_view()(request)
        self.assertTemplateUsed("malaria/edit_post.html")
        self.assertEqual(response.status_code, 200)

    def test_delete_posts_view(self):
        self.assertTemplateUsed("/malaria/list_posts")

    def test_view_posts_view(self):
        self.assertTemplateUsed("malaria/view_post.html")

    def test_list_app_users_view(self):
        self.assertTemplateUsed("malaria/list_app_users.html")
