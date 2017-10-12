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
    swap(0, pivotPosition, arr)
    return pivotPosition

def partition(arr):
    if(len(arr) == 1):
        return arr

    chosePivot(arr)

    low = 1
    high = len(arr)-1

    printArray(arr, low, high)

    done = False

    while not done:

        while(arr[low] < arr[0] and low<high):
            low+=1
            printArray(arr, low, high)

        while(arr[high] > arr[0] and low<high):
            high-=1
            printArray(arr, low, high)


        swap(low, high, arr)

        if(low >= high-1):
            done = True
            break

        low+=1
        high-=1

        printArray(arr, low, high)

    print('Partitioning done, inserting pivot at position')
    if(low == high and low < len(arr)-1):
            swap(0, low-1, arr)
    else:
        swap(0, low, arr)

    print(arr)

if __name__ == '__main__':
    arr = init()
    partition(arr)
