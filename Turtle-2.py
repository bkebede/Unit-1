Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> ben = turtle.Turtle()
>>> ben.color("brown")
>>> ben.pensize(1)
>>> ben.begin_fill()
>>> ben.right(90)
>>> ben.forward(70)
>>> ben.right(90)
>>> ben.forward(33)
>>> ben.undo()
>>> ben.forward(40)
>>> ben.undo()
>>> ben.undo()
>>> ben.undo()
>>> ben.forward(100)
>>> ben.undo()
>>> ben.forward(130)
>>> ben.right(90)
>>> ben.forward(40)
>>> ben.right(90)
>>> ben.forward(130)
>>> ben.end_fill()
>>> ben.position()
(-40.00,0.00)
>>> ben.goto(-20,0)
>>> ben.color("darkgreen")
>>> ben.shapesize(5,5,5)
>>> ben.undo()
>>> ben.shapesize(5,5,10)
>>> ben.undo()
>>> ben.shapesize(8,8,10)
>>> ben.position()
(-20.00,0.00)
>>> ben.goto(-20,40)
>>> ben.stamp()
7
>>> ben.goto(-20,60)
>>> ben.undo()
>>> ben.goto(-20,80)
>>> ben.stamp()
8
>>> ben.goto(-20,100)
>>> ben.undo()
>>> ben.goto(-20,120)
>>> 
