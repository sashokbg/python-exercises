import random

class RandomArray:
    """ An utility that allows you to create an array of random integers with arbitrary length"""
    
    numbers = []
    length = 0

    def init(self):
        i = 0
        while i < self.length:
            self.numbers.append(random.randint(0,9))
            i+=1

    def __init__(self, length):
        self.length = length
        self.init()

    def printNumbers(self):
        for i in range(len(self.numbers)):
            print("{} ".format(self.numbers[i]), end='')
        print()

    def __iter__(self):
        return self.numbers.__iter__()
    
    def __getitem__(self, key):
        return self.numbers.__getitem__(key)

    def __len__(self):
        return self.numbers.__len__()

    def __setitem__(self, key, value):
        return self.numbers.__setitem__(key, value)

    def __str__(self):
        asString = ''
        for i in range(len(self.numbers)):
             asString+=str(self.numbers[i])+' '
        return asString
