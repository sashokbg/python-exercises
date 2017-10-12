import unittest
from randomArray import RandomArray

class ToStringTest(unittest.TestCase):

    def test_should_return_numbers_as_string(self):
        arr = RandomArray(3)
        arr.numbers = [0, 1, 2]

        self.assertTrue(arr.__str__() == '0 1 2 ')
