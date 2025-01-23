"""Tests for class UnsortedArray"""
import unittest
from Arrays.python.unsorted_array import UnsortedArray

class TestArray(unittest.TestCase):
    """Tests for class UnsortedArray

        This test class contains unit tests for the UnsortedArray class.
    """

    # __repr__

    def test_repr(self):
        """Test string representation."""
        array = UnsortedArray(5, 'i')
        array.insert(1)
        array.insert(2)
        self.assertEqual(repr(array), "UnsortedArray(array('i', [1, 2]))")

    # __get_item__

    def test_getitem_valid_index(self):
        array = UnsortedArray(5, 'i')

        array.insert(1)
        array.insert(2)
        self.assertEqual(array[0], 1)
        self.assertEqual(array[1], 2)
