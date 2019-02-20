import unittest
from app.models import User,Pitch

class TestUsers(unittest.TestCase):

    def setUp(self):

        self.new_user = User(username = "watimakhanu@gamil.com", password = "1234")

    def test_instance(self):

        self.assertTrue(isinstance(self.new_user, User))

    def test_init(self):


        self.assertEquals(self.new_user.username,"watimakhanu@gamil.com")

    def test_password_generate(self):


        self.assertTrue(self.new_user.pass_locked is not None)

    def test_password_is_hashed(self):

        self.assertTrue(self.new_user.pass_locked is not "1234")

    def test_password_verifier(self):

        self.assertTrue(self.new_user.verify_pass("watimakhanu@gmail.com"))

    def test_save_user(self):

        self.new_user.save_user()
        users = User.query.all()
        self.assertTrue(len(users) > 0)
