import unittest
from binsearch import *
import numpy as np


class TestBinSearch(unittest.TestCase):
	"""
	The following test cases assume that:
	* The input list is sorted (thus its elements are comparable)
	"""

	def test_inf(self):
		self.assertEqual(binary_search([1, np.inf], 1), 0)
		self.assertEqual(binary_search([1, 2, np.inf], np.inf), 2)

	def test_nan(self):
		self.assertEqual(binary_search(['a', 'b', 'c','d', 'e'], 'b'), 1)

	def test_boundary(self):
		self.assertEqual(binary_search([], 1), -1)
		self.assertEqual(binary_search([2], 2), 0)
		self.assertEqual(binary_search([3], 2), -1)
		self.assertEqual(binary_search([1,2,3,4], 1), 0)
		self.assertEqual(binary_search([1,2,3,4], 4), 3)

	def test_not_found(self):
		self.assertEqual(binary_search(range(10), 11), -1)
		self.assertEqual(binary_search(range(10), -1), -1)
		self.assertEqual(binary_search(range(10), 4.5), -1)

	def test_range_parameter(self):
		self.assertEqual(binary_search([3,3,5,6,7,8], 3, 1), 1)
		self.assertEqual(binary_search(range(10), 5, 0, 3), -1)
		self.assertEqual(binary_search(range(10), 4, 2, 1), -1)


if __name__ == '__main__':
	unittest.main()