import math
import unittest

from simpson import simpson


class TestSimpson(unittest.TestCase):
    def test_sin(self):
        self.assertAlmostEqual(simpson(math.sin, 0, math.pi), 2.0, places=5)

    def test_polynomial_exact(self):
        # Simpson chính xác với đa thức bậc <= 3: tích phân x^2 trên [0, 3] = 9
        self.assertAlmostEqual(simpson(lambda x: x**2, 0, 3, n=2), 9.0, places=8)

    def test_odd_n_raises(self):
        with self.assertRaises(ValueError):
            simpson(lambda x: x, 0, 1, n=3)

    def test_non_positive_n_raises(self):
        with self.assertRaises(ValueError):
            simpson(lambda x: x, 0, 1, n=0)


if __name__ == "__main__":
    unittest.main()