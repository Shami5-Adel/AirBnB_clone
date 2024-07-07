#!/usr/bin/python3
"""Unittest module for the Review class."""

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Test Cases for the Review class."""

    def setUp(self):
        """Set up for testing Review."""
        self.review = Review()

    def test_instance_creation(self):
        """Test that an instance of Review is created."""
        self.assertIsInstance(self.review, Review)

    def test_attrs(self):
        """Test that Review has necessary attributes."""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

if __name__ == "__main__":
    unittest.main()
