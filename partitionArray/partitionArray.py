from randomArray.randomArray import RandomArray

def init():
    arr = RandomArray(10)
    print(arr)
    return arr

def printArray(arr, low, high):
    for i in range(len(arr)):
        if  (i == low):
            print('L ', end='')
        elif(i == high):
            print('H ', end='')
        else:
            print('  ', end='')
    print()
    print(arr)

def swap(i, j, arr):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def chosePivot(arr, start, end):
    pivotPosition = (abs(start-end)//2)+start;
    return pivotPosition, arr[pivotPosition]

def partition(arr, start, end):
    pivotPosition, pivotValue = chosePivot(arr, start, end)

    low = start
    high = end
    i = start

    while i <= high:
        if(arr[i] < pivotValue):
            swap(i, low, arr)
            i+=1
            low+=1
        elif(arr[i] > pivotValue):
            swap(i, high, arr)
            high-=1
        else:
            i+=1

    return low

if __name__ == '__main__':
    arr = init()
    partition(arr)
