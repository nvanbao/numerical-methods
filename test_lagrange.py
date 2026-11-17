import unittest

from lagrange import lagrange


class TestLagrange(unittest.TestCase):
    def test_quadratic(self):
        # đi qua (0,1), (1,3), (2,7) => P(x) = x^2 + x + 1
        self.assertAlmostEqual(lagrange([0, 1, 2], [1, 3, 7], 1.5), 4.75, places=8)

    def test_passes_through_nodes(self):
        xs, ys = [0, 1, 2], [1, 3, 7]
        for x, y in zip(xs, ys):
            self.assertAlmostEqual(lagrange(xs, ys, x), y, places=8)

    def test_linear(self):
        self.assertAlmostEqual(lagrange([0, 2], [1, 5], 1), 3.0, places=8)

    def test_length_mismatch_raises(self):
        with self.assertRaises(ValueError):
            lagrange([0, 1], [1], 0.5)

    def test_duplicate_x_raises(self):
        with self.assertRaises(ValueError):
            lagrange([1, 1], [2, 3], 1.5)


if __name__ == "__main__":
    unittest.main()