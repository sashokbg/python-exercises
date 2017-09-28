from randomArray.randomArray import RandomArray

randArr = RandomArray(10)
randArr.printNumbers()

sortedIndex = 0
min = randArr[sortedIndex]
minIndex = sortedIndex

def swap(randArr,index1,index2):
    tmp = randArr[index1]
    randArr[index1] = randArr[index2]
    randArr[index2] = tmp

def findMinIn(randArr,fromIndex):
    min = randArr[fromIndex]
    minIndex = fromIndex
    for i in range(fromIndex,len(randArr)):
        if randArr[i] < min:
            min = randArr[i]
            minIndex = i
    return minIndex

while sortedIndex < len(randArr)-1 :
    minIndex = findMinIn(randArr,sortedIndex)

    swap(randArr,minIndex,sortedIndex)
    sortedIndex+=1

print("Sorted:")
randArr.printNumbers()

    
