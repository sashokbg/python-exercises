from randomArray.randomArray import RandomArray 
from tools.swap import swap
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("numberOfElements", type=int, help="The number of random elements to generate")

args= parser.parse_args()

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
            swap(i, i+1, numbers)

        i = i+1

print(numbers)
