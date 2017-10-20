from randomArray.randomArray import RandomArray
from tools.swap import swap

randArr = RandomArray(10)
randArr.printNumbers()

sortedIndex = 0
min = randArr[sortedIndex]
minIndex = sortedIndex

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

    swap(minIndex,sortedIndex,randArr)
    sortedIndex+=1

print("Sorted:")
randArr.printNumbers()

    
