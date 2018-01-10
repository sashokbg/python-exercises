import turtle
from drawer import Drawer

class TurtleDrawer(Drawer):
    scale = 40

    def __init__(self):
        Drawer.__init__(self)
        turtle.speed(10)
    
    def draw(self):
        turtle.home()
        turtle.clear()

        for vector in self.system.vectors:
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

        for i in range(abs(vector.elements[1])):
            turtle.dot(3)
            if vector.elements[1]<0:
                turtle.write(-i, align='right')
                turtle.sety(-self.scale*(i+1))

            else:
                turtle.write(i, align='right')
                turtle.sety(self.scale*(i+1))

        turtle.home()
 
