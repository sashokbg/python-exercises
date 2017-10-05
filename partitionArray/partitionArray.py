arr = [5,4,8,9,6,3,7]

low = 1
high = len(arr)-1


done = False

def swap(i, j, arr):
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

    swap(low-1, high, arr)
    low+=1
    high-=1

swap(0, low, arr)

print(arr)
