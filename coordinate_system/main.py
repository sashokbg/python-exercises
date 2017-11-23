import turtle
from coordinate_system import CoordinateSystem
from vector.vector import Vector

system = CoordinateSystem(10, 10)
v1 = Vector([2,3], color="green")
v2 = Vector([6,-3], color="blue")
#v3 = v1.subvector(1)
system.add_vector(v1)
system.add_vector(v2)
system.print_system()
#system.transform(Vector([0,1]), Vector([-1, 0]))
#system.print_system()
system.transform(Vector([-1, 0]), Vector([0, -1]))
system.print_system()
turtle.done()
