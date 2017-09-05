from randomArray.randomArray import RandomArray

randArr = RandomArray(10)
randArr.printNumbers()
arr = randArr.numbers

sortedIndex = 0
min = arr[sortedIndex]
minIndex = sortedIndex

def swap(arr,index1,index2):
    tmp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = tmp

def findMinIn(arr,fromIndex):
    min = arr[fromIndex]
    minIndex = fromIndex
    for i in range(fromIndex,len(arr)):
        if arr[i] < min:
            min = arr[i]
            minIndex = i
    return minIndex

while sortedIndex < len(arr)-1 :
    minIndex = findMinIn(arr,sortedIndex)

    swap(arr,minIndex,sortedIndex)
    sortedIndex+=1

print("Sorted:")
randArr.printNumbers()

    
