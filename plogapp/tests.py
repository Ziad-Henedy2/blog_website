from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import post

# Create your tests here.

class blogtest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user( 
            username="test_user",email="test@gamil.com", password="1234")
        
        cls.post = post.objects.create(
            title = "test_title",
            author = cls.user,
            body = "test_body"
        )
    
    def test_post_model(self):
        self.assertEqual(self.post.title , "test_title")
        self.assertEqual(self.post.author.username , "test_user")
        self.assertEqual(self.post.body, "test_body")
        self.assertEqual(str(self.post),"test_title")
        self.assertEqual(self.post.get_absoulute_url(), "/post/1/")

    def test_url_home_are_exists_in_correct_location(self):
        responce = self.client.get("/")
        self.assertEqual(responce.status_code , 200)
         
    def test_post_details_are_in_correct_location(self):
        responce = self.client.get("/post/1/")
        self.assertEqual(responce.status_code,200)

    def test_post_postList(self):
        responce = self.client.get(reverse("home"))
        self.assertEqual(responce.status_code,200)
        self.assertContains(responce,"test_body")
        self.assertTemplateUsed(responce ,"home.html")
    
    def test_post_post_details(self):
        responce = self.client.get(reverse("post_details",kwargs={"pk":self.post.pk}))
        no_responce = self.client.get("/post/10000/")
        self.assertEqual(responce.status_code,200)
        self.assertEqual(no_responce.status_code,404)
        self.assertContains(responce , "test_body")
        self.assertTemplateUsed(responce , "post_detail.html")