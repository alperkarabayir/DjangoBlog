from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Topic, Post, User
from django.urls import reverse
from django.test.client import Client


# Models
class ModelTest(TestCase):
    """Testing models by creating and calling them"""
    def setUp(self):
        # create and save a User object.
        user = User(username='alper', password='test1234')
        user.save()

        # create a Topic model object in temporary database.
        topic = Topic(topic_name='django')
        topic.save()

        # create a Topic model object in temporary database.
        post = Post(title='test', content='testtesttest', author=user, topic_name=topic)
        post.save()

    def test_user_models(self):
        user = User.objects.get(username='alper')
        self.assertEqual(user.password, 'test1234')

    def test_topic_models(self):
        topic = Topic.objects.get(topic_name='django')
        self.assertEqual(topic.topic_name, 'django')

    def test_post_models(self):
        post = Post.objects.get(title='test')
        self.assertEqual(post.content, 'testtesttest')


class TopicListView(TestCase):
    """Checking Topic List by creating and calling by template"""
    @classmethod
    def setUpTestData(cls):
        # Create a topic for pagination tests
        Topic.objects.create(topic_name='django')

    def test_view_url_accessible_by_name(self):
        response = self.client.get('/topic/django')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/topic/django')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/topic_posts.html')


class UserPostListView(TestCase):
    """Testing User Posts List by creating a user and calling by template"""
    @classmethod
    def setUpTestData(cls):
        # Create a topic for pagination tests
        User.objects.create(username='alper', password="test1234")

    def test_view_url_accessible_by_name(self):
        response = self.client.get('/user/alper')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/user/alper')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/user_posts.html')


class PostListView(TestCase):
    """Testing Home Page link by creating a user, topic, posts and calling by template"""
    @classmethod
    def setUpTestData(cls):
        # Create a topic for pagination tests
        user = User.objects.create(username='alper', password="test1234")
        topic = Topic.objects.create(topic_name='django')
        post = Post.objects.create(title='test', content='testtesttest', author=user, topic_name=topic)

    def test_view_url_accessible_by_name(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')


class search(TestCase):
    """Search method testing"""
    def setUp(self):
        user = User.objects.create(username='alper', password="test1234")
        topic = Topic.objects.create(topic_name='django')
        post = Post.objects.create(title='test', content='testtesttest', author=user, topic_name=topic)

    def test_query_search_filter(self):
        self.assertQuerysetEqual(Post.objects.filter(title__icontains='test'), ["<Post: test>"])


class profile(TestCase):
    """Profile method testing with Logging In"""
    def setUp(self):
        self.client = Client()
        user = User.objects.create_user(username='alper', password="test1234")

    def test_view_uses_correct_template(self):
        self.client.login(username='alper', password='test1234')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/profile.html')

