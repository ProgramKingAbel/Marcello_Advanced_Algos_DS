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
    # max_size
    def test_max_size(self):
        array = UnsortedArray(3, 'i')
        self.assertEqual(array.max_size(), 3)
        array.insert(2)
        self.assertEqual(array.max_size(), 3)
        array = UnsortedArray(6, 'f')
        self.assertEqual(array.max_size(), 6)


        # __insert__

    def test_insert_valid(self):
        """Test inserting into an array with space"""
        array = UnsortedArray(5)
        array.insert(1)
        self.assertEqual(len(array), 1)
        self.assertEqual(array[0], 1)