import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("rows",help = "Number of total dice rows to do for the simulation", type=int)
args = parser.parse_args()

counter = 0
finalResult = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
throws = args.rows

def rollDice():
    return random.randint(1,6)

for i in range(throws):
    counter+=1 # counter = counter +1
    result = rollDice()
    numberOfSixes = 0

    while(result==6):
        hasAtleastOne6 = True        

        result = rollDice()
        finalResult[numberOfSixes][0]+=1
        numberOfSixes+=1

    numberOfSixes = 0

print("\ndone")

print("Total number of throws - {}".format(throws))
print("Sixes in a row   | Percentage    | Total hits")
print("---------------------------------------------")

for i in range(len(finalResult)):
    print("{0:d}\t\t | {1:.10f}\t | {2:d}".format((i+1),(finalResult[i][0]/throws), finalResult[i][0]))


