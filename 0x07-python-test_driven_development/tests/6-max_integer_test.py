#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxIntegerFunction(unittest.TestCase):
    
    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)
    
    def test_positive_integers(self):
        result = max_integer([1, 3, 5, 2, 4])
        self.assertEqual(result, 5)
    
    def test_negative_integers(self):
        result = max_integer([-1, -3, -5, -2, -4])
        self.assertEqual(result, -1)
    
    def test_mixed_integers(self):
        result = max_integer([-1, 3, 0, 2, -4])
        self.assertEqual(result, 3)
    
    def test_duplicate_integers(self):
        result = max_integer([3, 3, 3, 3])
        self.assertEqual(result, 3)
    
    def test_single_element(self):
        result = max_integer([7])
        self.assertEqual(result, 7)

    def test_mixed_types(self):
        result = max_integer([1, 'a', 3, 'b', 2])
        self.assertIsNone(result)
        
if __name__ == '__main__':
    unittest.main()
