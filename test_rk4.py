import math
import unittest

from rk4 import rk4


class TestRK4(unittest.TestCase):
    def test_exponential(self):
        # y' = y, y(0) = 1 => y(1) = e
        self.assertAlmostEqual(rk4(lambda x, y: y, 0, 1, 1, n=10), math.e, places=4)

    def test_polynomial_exact(self):
        # y' = 3x^2, y(0) = 0 => y(2) = 8 (RK4 chính xác với đa thức bậc thấp)
        self.assertAlmostEqual(rk4(lambda x, y: 3 * x**2, 0, 0, 2, n=4), 8.0, places=8)

    def test_more_accurate_than_euler_step(self):
        # cùng n = 10, sai số của RK4 phải nhỏ hơn nhiều so với Euler (≈ 0.12)
        error = abs(rk4(lambda x, y: y, 0, 1, 1, n=10) - math.e)
        self.assertLess(error, 1e-4)

    def test_invalid_n_raises(self):
        with self.assertRaises(ValueError):
            rk4(lambda x, y: y, 0, 1, 1, n=0)


if __name__ == "__main__":
    unittest.main()