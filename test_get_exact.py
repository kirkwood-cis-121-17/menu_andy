import unittest
from BetterProject import get_Exact

class TestGetExact(unittest.TestCase):
    def test_zero_zero_45(self):
        self.assertEqual( get_Exact(0,0,45), ("cos(45)","sin(45)"))

unittest.main()
