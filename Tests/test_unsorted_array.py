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

    def test_insert_in_full_array(self):
        """Test insert into a full array"""
        array = UnsortedArray(1)
        array.insert(1)
        with self.assertRaises(ValueError):
            array.insert(2)

    # delete

    def test_delete_valid(self):
        """Test deleting from an array with elements"""
        array = UnsortedArray(5)
        array.insert(1)
        array.insert(2)
        array.insert(3)
        array.insert(4)
        array.delete(1)

        self.assertEqual(len(array), 3)
        self.assertEqual(array[1], 4)
        array.delete(2)
        self.assertEqual(len(array), 2)
        self.assertEqual(array[0], 1)
        self.assertEqual(array[1], 4)
        array.delete(0)
        self.assertEqual(len(array), 1)
        self.assertEqual(array[0], 4)
        array.delete(0)
        self.assertEqual(len(array), 0)

    def test_delete_invalid_empty(self):
        """Test deleting from an empty array"""
        array = UnsortedArray(3)
        with self.assertRaises(ValueError):
            array.delete(0)

    def test_delete_invalid_index(self):
        """Test deleting with invalid index"""
        array = UnsortedArray(5)
        array.insert(1)

        with self.assertRaises(ValueError):
            array.delete(1)

        with self.assertRaises(ValueError):
            array.delete(-1)

    def test_find_present(self):
        """Test finding an entry that is present in the array"""
        array = UnsortedArray(7)
        array.insert(10)
        array.insert(-2)
        array.insert(5)

        self.assertEqual(array.find(-2), 1)
        self.assertEqual(array.find(5), 2)
        self.assertEqual(array.find(10), 0)

    def test_find_absent(self):
        """Test finding an entry that is absent from the array"""
        array = UnsortedArray(5)
        array.insert(7)
        array.insert(5)
        array.insert(48)

        index = array.find(81)

        self.assertEqual(index, None)

    def test_traverses_entire_array(self):
        result = []

        def test_callback(i: int):
            result.append(i + 1)

        array = UnsortedArray(5)
        array.insert(3)
        array.insert(4)
        array.insert(5)

        array.traverse(test_callback)
        self.assertEqual(result, [4, 5, 6])

    def test_get_minimum_value(self):
        """Test getting the minimum value in the array"""
        array = UnsortedArray(3)

        array.insert(8)
        array.insert(9)
        array.insert(10)

        self.assertEqual(array.min_in_array(), (8, 0))

    def test_get_minimum_value_negatives(self):
        array = UnsortedArray(3)

        array.insert(-8)
        array.insert(-9)
        array.insert(-10)

        self.assertEqual(array.min_in_array(), (-10, 2))

    def test_get_maximum_value(self):
        array = UnsortedArray(3)

        array.insert(8)
        array.insert(9)
        array.insert(10)

        self.assertEqual(array.max_in_array(), (10, 2))

    def test_get_maximum_minimum_value(self):
        array = UnsortedArray(3)

        array.insert(8)
        array.insert(9)
        array.insert(10)

        self.assertEqual(array.max_min_in_arr(), (10, 8))