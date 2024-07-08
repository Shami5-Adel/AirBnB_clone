#!/usr/bin/python3
"""Unittest module for the Amenity class."""

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test Cases for the Amenity class."""

    def setUp(self):
        """Set up for testing Amenity."""
        self.amenity = Amenity()

    def test_instance_creation(self):
        """Test that an instance of Amenity is created."""
        self.assertIsInstance(self.amenity, Amenity)

    def test_attrs(self):
        """Test that Amenity has a name attribute."""
        self.assertTrue(hasattr(self.amenity, "name"))

if __name__ == "__main__":
    unittest.main()
