import unittest
from add_digits import Solution

class TestDigits(unittest.TestCase):

    def test_add_digits(self):
        sol = Solution()

        #sol.addDigits(11)

    def test_add_digits(self):
        num = 1234

        for i in range(4):
            print('num {}'.format(num))
            digit = num - (num % 10**i)

            print(digit)

