import math
import unittest

from trapezoid import trapezoid


class TestTrapezoid(unittest.TestCase):
    def test_sin(self):
        self.assertAlmostEqual(trapezoid(math.sin, 0, math.pi, n=1000), 2.0, places=5)

    def test_linear_exact(self):
        # Hình thang chính xác với hàm bậc nhất: tích phân x trên [0, 2] = 2
        self.assertAlmostEqual(trapezoid(lambda x: x, 0, 2, n=1), 2.0, places=8)

    def test_quadratic(self):
        # tích phân x^2 trên [0, 3] = 9
        self.assertAlmostEqual(trapezoid(lambda x: x**2, 0, 3, n=1000), 9.0, places=4)

    def test_more_intervals_more_accurate(self):
        coarse = abs(trapezoid(math.sin, 0, math.pi, n=10) - 2.0)
        fine = abs(trapezoid(math.sin, 0, math.pi, n=1000) - 2.0)
        self.assertLess(fine, coarse)

    def test_invalid_n_raises(self):
        with self.assertRaises(ValueError):
            trapezoid(lambda x: x, 0, 1, n=0)


if __name__ == "__main__":
    unittest.main()