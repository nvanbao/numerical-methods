import math
import unittest

from euler import euler


class TestEuler(unittest.TestCase):
    def test_exponential(self):
        # y' = y, y(0) = 1 => y(1) = e
        self.assertAlmostEqual(euler(lambda x, y: y, 0, 1, 1, n=1000), math.e, places=2)

    def test_constant_slope(self):
        # y' = 2, y(0) = 1 => y(3) = 7 (Euler chính xác với đường thẳng)
        self.assertAlmostEqual(euler(lambda x, y: 2, 0, 1, 3, n=10), 7.0, places=8)

    def test_more_steps_more_accurate(self):
        coarse = abs(euler(lambda x, y: y, 0, 1, 1, n=10) - math.e)
        fine = abs(euler(lambda x, y: y, 0, 1, 1, n=1000) - math.e)
        self.assertLess(fine, coarse)

    def test_invalid_n_raises(self):
        with self.assertRaises(ValueError):
            euler(lambda x, y: y, 0, 1, 1, n=0)


if __name__ == "__main__":
    unittest.main()