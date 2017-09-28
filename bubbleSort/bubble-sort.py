from randomArray.randomArray import RandomArray 

def swap(numbers, pos1, pos2):
    tmp = numbers[pos1]
    numbers[pos1] = numbers[pos2]
    numbers[pos2] = tmp

numbers = RandomArray(5)
numbers.printNumbers()

print("Starting sorting..")

isDone  = False
while not isDone:
    i = 0
    isDone = True
    while i < len(numbers)-1:
        num1 = numbers[i]
        num2 = numbers[i+1]
    
        if(num1>num2):
            print('Swapping numbers {} {}'.format(num1, num2))
            isDone  = False
            swap(numbers, i, i+1)

        print('Is done - {}'.format(isDone))
        i = i+1
    print('Ended iteration. Is done {}'.format(isDone))

for i in range(len(numbers)):
    print(numbers[i])

#randomArray.numbers = numbers
#randomArray.printNumbers()

