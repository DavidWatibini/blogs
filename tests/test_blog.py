import unittest
from app.models import Blog,User

class TestBlog(unittest.TestCase):

    def setUp(self):

        self.new_user = User(username = "watimakhanu@gmail.com")
        self.new_blog = Blog(topic = "Tech", user = self.new_user)

    def test_instance(self):

        self.assertTrue(isinstance(self.new_blog,Blog))

    def test_init(self):

        self.assertEquals(self.new_blog.topic, "Tech")

    def test_save_blog(self):

        self.new_blog.save_blog()
        blogs = Blog.query.all()
        self.assertTrue(len(blogs) > 0)

    def test_relationship_user(self):

        user = self.new_blog.user.username
        self.assertTrue(username == "watimakhanu@gmail.com")
