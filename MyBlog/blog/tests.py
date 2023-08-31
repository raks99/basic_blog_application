from django.test import TestCase
from django.urls import reverse
from .models import Post
import unittest

"""
Run the tests:
python manage.py test blog.tests
"""
# Create your tests here.

# Testing polst list view- simulating HTTP requests and checking the responses
class PostListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create some test data to be used across the test methods
        Post.objects.create(title='TestPost 1', content='TestContent 1')
        Post.objects.create(title='TestPost 2', content='TestContent 2')
    
    def test_post_list_view_status_code(self):
        url = reverse('blog:post_list')  # 'post_list' is the name of the URL pattern
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # we test that the response matches 200. 200 = successful response
    
    def test_post_list_view_template_used(self):
        url = reverse('blog:post_list')  # 'reverse' is used to generate URLs by their name, ensuring future URL changes won't break the tests
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'blog/post_list.html')  # Test that post_list.html template was used
    
    def test_post_list_view_contains_posts(self):
        url = reverse('blog:post_list')  
        # make a GET request to the URL provided as an argument
        response = self.client.get(url)  #  self.client attribute that allows you to simulate HTTP requests,
        self.assertContains(response, 'TestPost 1')
        self.assertContains(response, 'TestPost 2')
        post = Post.objects.get(title='TestPost 1')
        self.assertIsNotNone(post.created_at)  # Check if creation date is not None
        post = Post.objects.get(title='TestPost 2')
        self.assertIsNotNone(post.created_at)


# Testing post detail view-
class PostDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test post
        cls.test_post = Post.objects.create(title='TestPost', content='TestContent')
    
    def test_post_detail_view_status_code(self):
        # Django's URL resolver will generate the appropriate URL for the PostDetailView view
        url = reverse('blog:post_detail', args=[self.test_post.pk])  # passing the PK of the self.test_post object as argument
        # each instance of the Post model has a PK associated with it. With PK we can identify that post (record)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_post_detail_view_template_used(self):
        url = reverse('blog:post_detail', args=[self.test_post.pk])
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'blog/post_detail.html')
    
    def test_post_detail_view_contains_post(self):
        url = reverse('blog:post_detail', args=[self.test_post.pk])
        response = self.client.get(url)
        self.assertContains(response, 'TestPost')  # we check that response Object have the "TestPost" presented
        self.assertContains(response, 'TestContent')


# Testing post create view-
class PostCreateViewTest(TestCase):
    def test_post_create_view_status_code(self):
        url = reverse('blog:post_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_post_create_view_template_used(self):
        url = reverse('blog:post_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'blog/post_form.html')
    
    def test_post_create_view_form_submission(self):
        url = reverse('blog:post_create')
        data = {'title': 'New Post', 'content': 'New Content'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Expect a redirect after successful form submission
        # 302 means "Found" and is used for redirection which means that the view is redirecting the user after a successful action
        new_post = Post.objects.get(title='New Post')
        self.assertIsNotNone(new_post)  # It is used to verify that a certain variable or object has been successfully created

# Similarly, you can add tests for PostUpdateViewTest and PostDeleteViewTest

class PostSearchViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create some test data for searching
        Post.objects.create(title='Python Post', content='Python Content')  #Post Django model, every model has an attribute "object" .create is method
        Post.objects.create(title='Django Post', content='Django Content')
    
    def test_post_search_view_status_code(self):
        url = reverse('blog:post_search')
        # simulate making an HTTP GET request to a specific URL with query parameters using Django's test client.
        # The first argument, url, is the URL you want to request. 
        response = self.client.get(url, {'q': 'Python'})  # argument, {'q': 'Python'}, is a dictionary of query parameters that you want to include in the request.
        self.assertEqual(response.status_code, 200)
    
    def test_post_search_view_template_used(self):
        url = reverse('blog:post_search')
        response = self.client.get(url, {'q': 'Python'})
        self.assertTemplateUsed(response, 'blog/post_search_results.html')
    
    def test_post_search_view_search_results(self):
        url = reverse('blog:post_search')
        response = self.client.get(url, {'q': 'Python'})
        self.assertContains(response, 'Python Post')
        self.assertNotContains(response, 'Django Post')

# And finally, test the REST API view
class PostAPITest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create some test data for the API view
        Post.objects.create(title='API Post 1', content='API Content 1')
        Post.objects.create(title='API Post 2', content='API Content 2')
    
    def test_post_api_view_status_code(self):
        url = reverse('blog:post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_post_api_view_contains_data(self):
        url = reverse('blog:post-list')
        response = self.client.get(url)
        self.assertContains(response, 'API Post 1')
        self.assertContains(response, 'API Post 2')
