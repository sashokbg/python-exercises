from vector.vector import Vector

class Matrix():

    size = 0
    rows = []

    def __init__(self, size):
        for i in range(size):
            elements = [None]*size
            self.rows.append(Vector(elements))

    def columns_size(self):
        return len(self.rows[0].elements)

    def rows_size(self):
        return len(self.rows)

