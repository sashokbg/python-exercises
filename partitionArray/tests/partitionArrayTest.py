import unittest
from partitionArray import *
from randomArray.randomArray import RandomArray

class PartitionArrayTest(unittest.TestCase):

    def checkArray(self, arr, pivot):
        pivotValue = arr[pivot]
        for i in range(0, pivot):
            if(arr[i] > pivotValue):
                self.fail('There are values that are bigger on the left side of the pivot at position {}'.format(i))
        for i in range(pivot, len(arr)):
            if(arr[i] < pivotValue):
                self.fail('There are values that are bigger on the left side of the pivot at position {}'.format(i))

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
        partition(arr)
        self.assertEqual(arr.numbers, [2, 0, 5, 7, 9])

    def test_array_of_1_element(self):
        arr = RandomArray(1)
        arr.numbers = [5]
        partition(arr)
        self.assertEqual(arr.numbers, [5])

    def test_pivot_is_last_value(self):
        arr = RandomArray(10)
        arr.numbers = [3, 4, 2, 0, 4, 8, 0, 4, 4, 1]
        partition(arr)

        self.checkArray(arr, 9)

    def test_repeating_pivot_value(self):
        arr = RandomArray(10)
        arr.numbers = [9, 0, 9, 5, 9]
        partition(arr)

        self.assertEqual(arr.numbers, [0, 9, 9, 9, 5])

if __name__ == '__main__':
    unittest.main()
