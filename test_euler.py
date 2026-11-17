import math
import unittest

from euler import euler


class TestEuler(unittest.TestCase):
    def test_exponential(self):
        # y' = y, y(0) = 1 => y(1) = e
        self.assertAlmostEqual(euler(lambda x, y: y, 0, 1, 1, n=1000), math.e, places=2)