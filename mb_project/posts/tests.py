from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='just a text')

    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_name=f'{post.text}'
        self.assertEqual(expected_object_name,'just a text')


class HomePageViewTest(TestCase):
    def setup(self):
        Post.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp=self.client.get('/')
        self.assertEqual(resp.status_code,200)

   
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
   
   
    def test_view_uses_correct_template(self):
            resp = self.client.get(reverse('home'))
            self.assertEqual(resp.status_code, 200)
            self.assertTemplateUsed(resp, 'home.html')