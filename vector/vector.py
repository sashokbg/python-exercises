class Vector():
    elements = []

    def __init__(self, elements):
        self.elements = elements

    def add(self, number):
        for i in range(len(self.elements)):
            self.elements[i]+=number

    def add_vector(self, vector):
        for i in range(len(vector.elements)):
            self.elements[i]+= vector.elements[i]

        return self
