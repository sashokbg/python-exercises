import math

class Vector():
    elements = []
    color = "black"
    is_primary = False

    def __init__(self, elements, color="black", is_primary = False):
        self.elements = elements
        self.color = color
        self.is_primary = is_primary

    def __getitem__(self, key):
        return self.elements.__getitem__(key)

    def __setitem__(self, key, value):
        self.elements.__setitem__(key, value)

    def add(self, number):
        for i in range(len(self.elements)):
            self.elements[i]+=number

    def add_vector(self, vector):
        for i in range(len(vector.elements)):
            self.elements[i]+= vector.elements[i]

        return self

    def magnitude(self):
        squared_sum = 0
        for element in self.elements:
            squared_sum += element**2

        return math.sqrt(squared_sum)


    def __str__(self):
        return str(self.elements)
