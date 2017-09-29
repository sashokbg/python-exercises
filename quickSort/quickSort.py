from randomArray.randomArray import RandomArray

print("Quicksort")

numbers = RandomArray(10)
numbers.printNumbers()

def partition(numbers):
    pivotPosition = len(numbers)//2 

    print("Pivot position is {}".format(pivotPosition))

    pivotValue = numbers[pivot]


    for i in range(0,pivotPosition):
        for j in range(len(numbers), pivotPosition):

            if(numbers[i]>pivotValue):
                swap()
