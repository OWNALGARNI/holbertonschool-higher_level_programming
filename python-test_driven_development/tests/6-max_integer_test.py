#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for the max_integer function."""

    def test_ordered_list(self):
        """Test a list with integers in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list with integers in random order."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when the max value is at the beginning of the list."""
        self.assertEqual(max_integer([10, 5, 3, 1]), 10)

    def test_single_element_list(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test an empty list should return None."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test a list with only negative integers."""
        self.assertEqual(max_integer([-5, -2, -9, -1]), -1)

    def test_mixed_positive_negative(self):
        """Test a list with mixed positive and negative integers."""
        self.assertEqual(max_integer([-10, 5, -3, 8, 0]), 8)

    def test_all_equal(self):
        """Test a list where all elements are equal."""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)
