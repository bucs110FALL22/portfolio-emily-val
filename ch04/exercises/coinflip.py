import random 
import turtle

myturtle = turtle.Turtle()
window = turtle.Screen()
myturtle.shape("turtle")
myturtle.color("purple")
myturtle.speed(0)

distance = 10
angle = 90
is_in_screen = True

while is_in_screen: 
  coin = random.randrange(0, 2)
  if coin == 0:
    myturtle.right(angle)
  else: 
    myturtle.left(angle)
  myturtle.forward(distance)

  turtleX = myturtle.xcor()
  turtleY = myturtle.ycor()
  x_range = window.window_width()/2
  y_range = window.window_height()/2

  if abs(turtleX) > x_range or abs(turtleY) > y_range:
    is_in_screen = False

window.bgcolor("lightblue")
window.exitonclick()
  
