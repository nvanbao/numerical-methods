import unittest

from newton import newton_raphson


class TestNewton(unittest.TestCase):
    def test_cubic_root(self):
        f = lambda x: x**3 - x - 2
        df = lambda x: 3 * x**2 - 1
        root, _ = newton_raphson(f, df, 1.5)
        self.assertAlmostEqual(root, 1.521380, places=4)

    def test_sqrt_two(self):
        root, _ = newton_raphson(lambda x: x**2 - 2, lambda x: 2 * x, 1)
        self.assertAlmostEqual(root, 2 ** 0.5, places=4)

    def test_zero_derivative_raises(self):
        with self.assertRaises(ZeroDivisionError):
            newton_raphson(lambda x: x**2 - 1, lambda x: 2 * x, 0)

    def test_invalid_tol_raises(self):
        with self.assertRaises(ValueError):
            newton_raphson(lambda x: x - 1, lambda x: 1, 0, tol=-1)


if __name__ == "__main__":
    unittest.main()