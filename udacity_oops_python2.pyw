import turtle
def draw_square():
	print "in the draw square function"
    window = turtle.Screen()
    window.bgcolor("red")
	
    brad = turtle.Turtle()
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90) 
    brad.forward(100)
    brad.right(90)
    window.exitonclick()
	
draw_square()
