from partitionArray.partitionArray import *
from randomArray.randomArray import RandomArray
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("numberOfElements", type=int, help="The number of random elements to generate")

args = parser.parse_args()

def quickSort(arr, start, end):
    if(start < end):
        pivot = partition(arr, start, end)
        quickSort(arr, start, pivot-1)
        quickSort(arr, pivot+1, end)

if __name__ == '__main__':
    arr = RandomArray(args.numberOfElements)
    print(arr)
    quickSort(arr, 0, len(arr)-1)
    print(arr)
