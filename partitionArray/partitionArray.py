arr = [5,4,8,9,6,3,7]

low = 1
high = len(arr)-1


done = False

def swap(i, j, arr):
    print('swapping {} and {}'.format(i,j))
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

while not done:

    if(low >= high):
        done = True

    while(arr[low] < arr[0] and low<high):
        low+=1
        print('low {}'.format(low))

    while(arr[high] > arr[0] and low<high):
        high-=1
        print('high {}'.format(high))

    swap(low, high, arr)

swap(0, high-1, arr)

print(arr)
