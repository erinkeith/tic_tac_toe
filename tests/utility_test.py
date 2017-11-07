import unittest
import utility


class TestBase3Conversion(unittest.TestCase):
    def test_one(self):
        self.assertEqual(utility.base3tobase10(0, 1), 1)

    def test_zero(self):
        self.assertEqual(utility.base3tobase10(0, 0), 0)

    def test_four(self):
        self.assertEqual(utility.base3tobase10(1, 1), 4)

    def test_eight(self):
        self.assertEqual(utility.base3tobase10(2, 2), 8)

    def test_out_of_bounds(self):
        self.assertIsNone(utility.base3tobase10(3, 3))