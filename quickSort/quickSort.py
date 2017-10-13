from partitionArray.partitionArray import *
from randomArray.randomArray import RandomArray

def quickSort(arr, start, end):
    if(start < end):
        pivot = partition(arr, start, end)
        quickSort(arr, start, pivot-1)
        quickSort(arr, pivot+1, end)

if __name__ == '__main__':
    arr = RandomArray(10)
    print(arr)
    quickSort(arr, 0, len(arr)-1)
    print(arr)
