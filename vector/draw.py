from vector import Vector
import turtle

scale = 40

def print_vector(vector, color):
    turtle.pencolor(color)
    turtle.penup()
    turtle.home()
    turtle.pendown()
    turtle.goto(vector.elements[0]*scale,vector.elements[1]*scale)

def print_system(x,y):
    turtle.home()
    for i in range(x):
        turtle.dot(3)
        turtle.write(i, align='right')
        turtle.setx(scale*(i+1))

    turtle.home()
    for j in range(y):
        turtle.dot(3)
        turtle.write(j, align='right')
        turtle.sety(scale*(j+1))

turtle.speed(10)
print_system(10,10)

vector1 = Vector([3, 2])

print_vector(vector1, 'red')

vector2 = Vector([1,-4])

print_vector(vector2, 'blue')

vector1.add_vector(vector2)

print_vector(vector1, 'green')

turtle.done()
