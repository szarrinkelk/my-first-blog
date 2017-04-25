from blog.models import Comment, Post
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import TestCase
from django.test import Client


class CommentTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id=1)
        self.post = Post.objects.create(author=self.user)
        self.comment = Comment.objects.create(text="Hello", post=self.post)
        self.client = Client()

    def test_comment_is_empty(self):
        with self.assertRaises(IntegrityError):
            self.assertEqual(self.comment.text, "Hello")

    def test_approval(self):
        self.comment.approve()
        self.assertEqual(self.comment.approved_comment, True)

    def test_context(self):
        self.post = Post.objects.create(author=self.user)
        self.post.publish()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['posts']), 1)