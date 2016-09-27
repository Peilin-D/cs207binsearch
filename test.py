import unittest
from binsearch import *
import numpy as np

class TestBinSearch(unittest.TestCase):

	def test_nan(self):
		with self.assertRaises(ValueError):
			binary_search([np.nan, 1, 2], 1)
			binary_search([np.nan, 1, 2], np.nan)

		with self.assertRaises(TypeError):
			binary_search(['a', 'b', 1, 2], 1)

		self.assertEqual(binary_search(['a', 'b', 'c'], 'b'), 1)

	def test_boundary(self):
		self.assertEqual(binary_search([], 1), -1)
		self.assertEqual(binary_search([1,2,3,4], 1), 0)
		self.assertEqual(binary_search([1,2,3,4], 4), 3)

	def test_not_found(self):
		self.assertEqual(binary_search(range(10), 11), -1)
		self.assertEqual(binary_search(range(10), -1), -1)
		self.assertEqual(binary_search([2,5,7,9], 4), -1)

if __name__ == '__main__':
	unittest.main()