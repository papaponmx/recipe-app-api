"""
Test for models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
    """Test models."""

    def test_create_user_with_email_succesful(self):
        """Test creating a user with an email succesful."""
        email = "test@example.com"
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users"""
        password = 'testpass123'
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@example.com', 'TEST3@example.com']
        ]

        for email, expected, in sample_emails:
            user = get_user_model().objects.create_user(
                email= email,
                password =password
                )
            self.assertEqual(user.email, expected)
    

    def test_create_superuser(self):
        """Test creating a super user."""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
