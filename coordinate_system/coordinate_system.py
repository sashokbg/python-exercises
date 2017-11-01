from vector.vector import Vector
import turtle

class CoordinateSystem():
    scale = 40
    vectors = []

    def __init__(self, x, y):
        xVector = Vector([0, x], is_primary=True)
        yVector = Vector([y, 0], is_primary=True)

        self.add_vector(xVector)
        self.add_vector(yVector)
        turtle.speed(10)

    def add_vector(self, vector):
        self.vectors.append(vector)

    def print_primary_vector(self, vector):
        print("Printing primary vector {}".format(vector))
        turtle.home()
        turtle.pendown()
        for i in range(abs(vector.elements[0])):
            turtle.dot(3)
            if vector.elements[0]<0:
                turtle.write(-i, align='right')
                turtle.setx(-self.scale*(i+1))
            else:
                turtle.write(i, align='right')
                turtle.setx(self.scale*(i+1))
            
        turtle.home()

        for i in range(abs(vector.elements[1])):
            turtle.dot(3)
            if vector.elements[1]<0:
                turtle.write(-i, align='right')
                turtle.sety(-self.scale*(i+1))
            
            else:
                turtle.write(i, align='right')
                turtle.sety(self.scale*(i+1))
        turtle.home()
        
    def print_system(self):
        print("printing system")
        turtle.clear()
        for vector in self.vectors:
            print(vector.is_primary)
            if vector.is_primary:
                self.print_primary_vector(vector)
            else:
                turtle.home()
                turtle.pencolor(vector.color)     
                turtle.penup()             
                turtle.home()              
                turtle.pendown()           
                turtle.goto(vector.elements[0]*self.scale,vector.elements[1]*self.scale)
                turtle.write('[{0:.2f}]'.format(vector.magnitude()))
                turtle.penup()
                turtle.home()

    def transform(self, v1, v2):
        for vector in self.vectors:
            vector[0]=vector[0]*v1[0] + vector[0]*v2[0]
            vector[1]=vector[1]*v1[1] + vector[1]*v2[1]

