from randomArray.randomArray import RandomArray

def init():
    arr = RandomArray(10)
    print(arr)
    return arr

def printArray(arr, low, high):
    for i in range(len(arr)):
        if(i == low or i == high):
            print('v ', end='')
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

        if(low >= high):
            done = True
            break

        swap(low, high, arr)
        low+=1
        high-=1

        printArray(arr, low, high)

    print('Partitioning done, inserting pivot at position')
    swap(0, low, arr)

    print(arr)

if __name__ == '__main__':
    arr = init()
    partition(arr)
