import math
import unittest

from simpson import simpson


class TestSimpson(unittest.TestCase):
    def test_sin(self):
        self.assertAlmostEqual(simpson(math.sin, 0, math.pi), 2.0, places=5)