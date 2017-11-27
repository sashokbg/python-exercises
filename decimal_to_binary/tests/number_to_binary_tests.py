import unittest
from decimal_to_binary.dtb import dtb

class TestDTB(unittest.TestCase):

    def test_convert_1(self):
        result = dtb(1)

        self.assertEqual(result, '1')

    def test_convert_2(self):
        result = dtb(2)

        self.assertEqual(result, '10')

    def test_convert_10(self):
        result = dtb(10)

        self.assertEqual(result, '1010')
