import turtle
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("purple")
distance = 50
angle = 90
my_turtle.forward(distance)
my_turtle.left(angle)
my_turtle.down()

my_turtle.forward(distance)
my_turtle.left(angle)
my_turtle.forward(distance)
my_turtle.left(angle)
my_turtle.forward(distance)
my_turtle.left(angle)

my_turtle.up()
my_turtle.forward(55)
my_turtle.color("red")
my_turtle.down()

my_turtle.forward(distance)
my_turtle.left(angle)
my_turtle.forward(distance)
my_turtle.left(angle)
my_turtle.forward(distance)
my_turtle.left(angle)
my_turtle.forward(distance)

window = turtle.Screen()
window.exitonclick()
