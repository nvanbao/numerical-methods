import unittest

from lagrange import lagrange


class TestLagrange(unittest.TestCase):
    def test_quadratic(self):
        # đi qua (0,1), (1,3), (2,7) => P(x) = x^2 + x + 1
        self.assertAlmostEqual(lagrange([0, 1, 2], [1, 3, 7], 1.5), 4.75, places=8)