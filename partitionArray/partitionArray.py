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
    print('swapping {}[{}] and {}[{}]'.format(i,arr[i],j,arr[j]))
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def chosePivot(arr):
    pivotPosition = len(arr)//2;
    print('Pivot value is {} at position {}'.format(arr[pivotPosition], pivotPosition))
    return pivotPosition, arr[pivotPosition]

def partition(arr):
    pivotPosition, pivotValue = chosePivot(arr)

    low = 0
    high = len(arr)-1
    i = 0
    printArray(arr, low, high)

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

        printArray(arr, low, high)

    print('Partitioning done, inserting pivot at position')
    print(arr)

if __name__ == '__main__':
    arr = init()
    partition(arr)
