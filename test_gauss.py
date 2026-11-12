import unittest

from gauss import gauss_elimination


class TestGauss(unittest.TestCase):
    def test_3x3(self):
        A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
        b = [8, -11, -3]
        x = gauss_elimination(A, b)
        for got, want in zip(x, [2, 3, -1]):
            self.assertAlmostEqual(got, want, places=6)