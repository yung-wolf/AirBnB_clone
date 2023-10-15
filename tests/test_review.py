import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):

    def test_attributes(self):
        """Test attributes of Review class"""
        s1 = Review()

        self.assertTrue(hasattr(s1, 'place_id'))
        self.assertTrue(hasattr(s1, 'user_id'))
        self.assertTrue(hasattr(s1, 'text'))
        self.assertIsInstance(s1.place_id, str)
        self.assertIsInstance(s1.user_id, str)
        self.assertIsInstance(s1.text, str)
