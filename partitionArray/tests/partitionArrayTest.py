import unittest
from partitionArray import chosePivot
from randomArray.randomArray import RandomArray

class PartitionArrayTest(unittest.TestCase):


    def test_should_define_pivot_in_middle_when_3_numbers(self):
        arr = RandomArray(3)
        arr.numbers = [0, 1, 2]
        pivotPosition = chosePivot(arr)

        self.assertTrue(pivotPosition == 1)

if __name__ == '__main__':
    unittest.main()
