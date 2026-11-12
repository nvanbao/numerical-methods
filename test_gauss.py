import unittest

from gauss import gauss_elimination


class TestGauss(unittest.TestCase):
    def test_3x3(self):
        A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
        b = [8, -11, -3]
        x = gauss_elimination(A, b)
        for got, want in zip(x, [2, 3, -1]):
            self.assertAlmostEqual(got, want, places=6)

    def test_2x2(self):
        x = gauss_elimination([[1, 1], [1, -1]], [3, 1])
        self.assertAlmostEqual(x[0], 2.0, places=6)
        self.assertAlmostEqual(x[1], 1.0, places=6)

    def test_needs_pivoting(self):
        # phần tử đầu bằng 0, phải đổi dòng mới giải được
        x = gauss_elimination([[0, 1], [1, 1]], [1, 2])
        self.assertAlmostEqual(x[0], 1.0, places=6)
        self.assertAlmostEqual(x[1], 1.0, places=6)