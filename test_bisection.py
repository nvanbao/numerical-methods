import unittest

from bisection import bisection


class TestBisection(unittest.TestCase):
    def test_cubic_root(self):
        root, _ = bisection(lambda x: x**3 - x - 2, 1, 2)
        self.assertAlmostEqual(root, 1.521380, places=4)

    def test_sqrt_two(self):
        root, _ = bisection(lambda x: x**2 - 2, 1, 2)
        self.assertAlmostEqual(root, 2 ** 0.5, places=4)

    def test_same_sign_raises(self):
        with self.assertRaises(ValueError):
            bisection(lambda x: x**2 + 1, 0, 1)

    def test_invalid_interval_raises(self):
        with self.assertRaises(ValueError):
            bisection(lambda x: x - 1, 2, 0)

    def test_invalid_tol_raises(self):
        with self.assertRaises(ValueError):
            bisection(lambda x: x - 1, 0, 2, tol=0)

    def test_midpoint_is_root(self):
        root, iters = bisection(lambda x: x - 1.5, 1, 2)
        self.assertEqual(root, 1.5)
        self.assertEqual(iters, 1)

    def test_max_iter_limit(self):
        _, iters = bisection(lambda x: x - 1.234567, 0, 10, tol=1e-12, max_iter=5)
        self.assertEqual(iters, 5)


if __name__ == "__main__":
    unittest.main()