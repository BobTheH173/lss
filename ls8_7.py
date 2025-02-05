import unittest
from ls8_6 import *


class My_Test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder(1, 2), 4)


if __name__ == "__main__":
    unittest.main()
