
#!/usr/bin/python3
"""Unittest module for the Place class."""

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test Cases for the Place class."""

    def setUp(self):
        """Set up for testing Place."""
        self.place = Place()

    def test_instance_creation(self):
        """Test that an instance of Place is created."""
        self.assertIsInstance(self.place, Place)

    def test_attrs(self):
        """Test that Place has necessary attributes."""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

if __name__ == "__main__":
    unittest.main()
