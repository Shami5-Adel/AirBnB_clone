#!/usr/bin/python3
"""Unittest module for the User class."""

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Test Cases for the User class."""

    def setUp(self):
        """Set up for testing User."""
        self.user = User()

    def test_instance_creation(self):
        """Test that an instance of User is created."""
        self.assertIsInstance(self.user, User)

    def test_attrs(self):
        """Test that User has email, password, first_name, last_name attributes."""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

if __name__ == "__main__":
    unittest.main()
