import unittest
from partitionArray import *
from randomArray.randomArray import RandomArray

class PartitionArrayTest(unittest.TestCase):

    def test_should_define_pivot_in_middle_when_5_numbers(self):
        arr = RandomArray(5)
        arr.numbers = [0, 1, 2, 3, 4]
        pivotPosition = chosePivot(arr)

        self.assertEqual(pivotPosition, 2)

    def test_should_define_pivot_in_1_when_4_numbers(self):
        arr = RandomArray(4)
        arr.numbers = [0, 1, 2, 4]
        pivotPosition = chosePivot(arr)

        self.assertEqual(pivotPosition,2)

    def test_repeating_numbers(self):
        arr = RandomArray(5)
        arr.numbers = [7, 7, 5, 3, 3]
        partition(arr)

        self.assertEqual(arr.numbers, [3, 3, 5, 7, 7])

    def test_same_number_array(self):
        arr = RandomArray(5)
        arr.numbers = [5, 5, 5, 5, 5]
        partition(arr)

        self.assertEqual(arr.numbers, [5, 5, 5, 5, 5])

    def test_pair_length_array(self):
        arr = RandomArray(6)
        arr.numbers = [2, 9, 5, 7, 0]


if __name__ == '__main__':
    unittest.main()
