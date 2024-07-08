#!/usr/bin/python3
"""Unittest module for the BaseModel class."""

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test Cases for the BaseModel class."""

    def setUp(self):
        """Set up for testing BaseModel."""
        self.model = BaseModel()

    def test_instance_creation(self):
        """Test that an instance of BaseModel is created."""
        self.assertIsInstance(self.model, BaseModel)

    def test_save_method(self):
        """Test the save method updates the updated_at attribute."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method creates a dictionary with proper attrs."""
        model_dict = self.model.to_dict()
        self.assertEqual(self.model.__class__.__name__, model_dict['__class__'])

if __name__ == "__main__":
    unittest.main()
