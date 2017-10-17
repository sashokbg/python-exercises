from python_tools.swap import *

arr = [1, 0, 2, 1, 2, 1, 0, 0, 1]

print(arr)
print('Sorting flag')

def printArray(arr, low, high):
    for i in range(len(arr)):
        if(i == low):
            print(' L ', end='')
        elif(i == high):
            print(' H ', end='')
        else:
            print('   ', end='')
    print()
    print(arr)

def sortFlag(arr):
    low = 0
    high = len(arr)-1
    i = 0

    while i <= high:
        print('i is {}'.format(i))
        print('low is {}'.format(low))
        print('high is {}'.format(high))
        if arr[i] == 0:
            swap(i, low, arr)
            low+=1
            i+=1
        elif arr[i] == 2:
            swap(i, high, arr)
            high-=1
        else:
            i+=1
        printArray(arr, low, high)

if __name__ == '__main__':
    sortFlag(arr)

