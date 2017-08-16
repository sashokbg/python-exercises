class RandomArray:
    """ An utility that allows you to create an array of random integers with arbitrary length"""
    
    numbers = []
    length = 0

    def init(self):
        i = 0
        while i < self.length:
            self.numbers.append(i)
            i+=1

    def __init__(self, length):
        self.length = length
        self.init()

    def printNumbers(self):
        for i in range(len(self.numbers)):
            print(self.numbers[i])

x = RandomArray(10)
print(x.__doc__)
x.printNumbers()

