"""
Test for models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test Models"""

    def test_create_user_With_email_successfull(self):
        """Test creating user"""
        self.email = 'test@example.com'
        self.password = 'testpass123'

        user = get_user_model().objects.create_user(
            email=self.email,
            password=self.password,
        )

        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))

    def test_user_email_normalized(self):
        sample_emails = [
            ['test1@Example.com', 'test1@example.com'],
            ['TeSt2@EXAMPLE.Com', 'TeSt2@example.com'],
            ['TEST3@example.COM', 'TEST3@example.com'],
            ['teST4@EXAMPLE.COM', 'teST4@example.com'],
        ]

        for email, expected in sample_emails:
            self.user = get_user_model().objects.create_user(
                email, 'testpass123'
                )
            self.assertEqual(self.user.email, expected)

    def test_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'pass123')

    def test_create_superuser(self):
        self.user = get_user_model().objects.create_superuser(
            'test@example.com',
            'testpass123'
        )

        self.assertTrue(self.user.is_superuser)
        self.assertTrue(self.user.is_staff)
