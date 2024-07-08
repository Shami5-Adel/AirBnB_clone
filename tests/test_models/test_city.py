#!/usr/bin/python3
"""Unittest module for the City class."""

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test Cases for the City class."""

    def setUp(self):
        """Set up for testing City."""
        self.city = City()

    def test_instance_creation(self):
        """Test that an instance of City is created."""
        self.assertIsInstance(self.city, City)

    def test_attrs(self):
        """Test that City has necessary attributes."""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

if __name__ == "__main__":
    unittest.main()
