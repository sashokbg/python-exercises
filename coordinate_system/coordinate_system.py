from vector.vector import Vector
from drawer import Drawer

class CoordinateSystem():
    vectors = []

    def __init__(self, x, y, drawer):
        xVector = Vector([0, x], is_primary=True)
        yVector = Vector([y, 0], is_primary=True)
        self.add_vector(xVector)
        self.add_vector(yVector)

        drawer.system = self
        self.drawer = drawer

    def add_vector(self, vector):
        self.vectors.append(vector)

    def print_system(self):
        print("printing system")
        self.drawer.draw()

    def transform(self, v1, v2):
        for vector in self.vectors:
            vector[0]=vector[0]*v1[0] + vector[0]*v2[0]
            vector[1]=vector[1]*v1[1] + vector[1]*v2[1]

