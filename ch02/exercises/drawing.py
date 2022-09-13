import turtle

sides = input("Pick a number of sides for the shape: ")
sides = int(sides)
length = input("Pick the length for each side of the shape: ")
length = int(length)
myturtle = turtle.Turtle()
myturtle.shape("turtle")
myturtle.color("purple")
for i in range(sides):
   myturtle.forward(length)
   myturtle.left(360/sides)

window = turtle.Screen()
window.exitonclick()
