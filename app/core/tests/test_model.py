"""Test fort models."""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests (TestCase):
    """TEst models."""

    def test_create_user_with_email_successful(self):
        '''Test creating a new user with an email is successful'''

        email = 'test@example.com'
        password = "testpass123"
        #   This will call the UserManager() method create_user from our custom User model, which we defined in users/models.py
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        #  assertTrue checks if the first argument is True
        self.assertEqual(user.email, email)
        #  check_password () method verifies that the plain text password matches
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""

        sample_emails = [
            ["test1@EXAMPLE.COM", "test1@example.com"],
            ["test2@ExAmpLE.cOm", "test2@example.com"],
            ["Test3@EXAMPLE.COM", "Test3@example.com"],
            ["test4@example.COM", "test4@example.com"]
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test creating user without an email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')
