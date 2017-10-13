from randomArray.randomArray import RandomArray 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("numberOfElements", type=int, help="The number of random elements to generate")

args= parser.parse_args()

def swap(numbers, pos1, pos2):
    tmp = numbers[pos1]
    numbers[pos1] = numbers[pos2]
    numbers[pos2] = tmp

numbers = RandomArray(args.numberOfElements)
print(numbers)

isDone  = False
while not isDone:
    i = 0
    isDone = True
    while i < len(numbers)-1:
        num1 = numbers[i]
        num2 = numbers[i+1]
    
        if(num1>num2):
            isDone  = False
            swap(numbers, i, i+1)

        i = i+1

print(numbers)
