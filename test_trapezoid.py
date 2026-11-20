import math
import unittest

from trapezoid import trapezoid


class TestTrapezoid(unittest.TestCase):
    def test_sin(self):
        self.assertAlmostEqual(trapezoid(math.sin, 0, math.pi, n=1000), 2.0, places=5)