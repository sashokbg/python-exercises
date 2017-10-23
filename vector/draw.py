from vector import Vector
import matplotlib.pyplot as plt

def draw_vector(vector, vcolor, field):
    field.arrow(0, 0, vector.elements[0], vector.elements[1], head_width=0.05, head_length=0.1, fc='k', ec='k', color=vcolor)

field = plt.axes()
vector1 = Vector([3, 2])
vector2 = Vector([1, 4])

vector1.add_vector(vector2)

draw_vector(vector1, '#0F0F0F', field)

plt.show()

