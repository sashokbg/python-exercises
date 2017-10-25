from vector import Vector
import turtle

def print_vector(vector, color):
    turtle.pencolor(color)
    turtle.penup()
    turtle.home()
    turtle.pendown()
    turtle.goto(vector.elements[0]*40,vector.elements[1]*40)

turtle.write(0)
turtle.setx(40)
turtle.write(1)

vector1 = Vector([3, 2])

print_vector(vector1, 'red')

vector2 = Vector([1, 4])

print_vector(vector2, 'blue')

vector1.add_vector(vector2)

print_vector(vector1, 'green')

turtle.done()
