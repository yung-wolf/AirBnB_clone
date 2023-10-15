import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):

    def test_name(self):
        """Test name attr of State class"""
        s1 = State()
        newyork = State()
        newyork.name = "NewYork"

        self.assertTrue(hasattr(s1, 'name'))
        self.assertTrue(hasattr(newyork, 'name'))
        self.assertEqual(newyork.name, 'NewYork')
        self.assertIsInstance(s1.name, str)
