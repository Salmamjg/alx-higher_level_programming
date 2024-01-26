#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxIntegerFunction(unittest.TestCase):
    """Test cases for the max_integer function."""
    
    def test_max_integer(self):
        """Test the max_integer function with a list of integers."""
        result = max_integer([1, 3, 5, 2, 4])
        self.assertEqual(result, 5)

    def test_empty_list(self):
        """Test the max_integer function with an empty list."""
        result = max_integer([])
        self.assertIsNone(result)
    
    def test_positive_integers(self):
        """Test the max_integer function with a list of positive numbers."""
        result = max_integer([1, 3, 5, 2, 4])
        self.assertEqual(result, 5)
    
    def test_negative_integers(self):
        """Test the max_integer function with a list of negative numbers."""
        result = max_integer([-1, -3, -5, -2, -4])
        self.assertEqual(result, -1)
    
    def test_mixed_integers(self):
        """Test the max_integer function with a list of mixed positive and negative numbers."""
        result = max_integer([-1, 3, 0, 2, -4])
        self.assertEqual(result, 3)
    
    def test_duplicate_integers(self):
        """Test the max_integer function with a list of duplicate numbers"""
        result = max_integer([3, 3, 3, 3])
        self.assertEqual(result, 3)
    
    def test_single_element(self):
        """Test the max_integer function with single element list"""
        result = max_integer([7])
        self.assertEqual(result, 7)

    def test_mixed_types(self):
        """Test the max_integer function with a mixed types list"""
        result = max_integer([1, 'a', 3, 'b', 2])
        self.assertIsNone(result)
        
if __name__ == '__main__':
    unittest.main()
