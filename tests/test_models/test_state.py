#!/usr/bin/python3
"""Unittest module for the State class."""

import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Test Cases for the State class."""

    def setUp(self):
        """Set up for testing State."""
        self.state = State()

    def test_instance_creation(self):
        """Test that an instance of State is created."""
        self.assertIsInstance(self.state, State)

    def test_attrs(self):
        """Test that State has a name attribute."""
        self.assertTrue(hasattr(self.state, "name"))

if __name__ == "__main__":
    unittest.main()
