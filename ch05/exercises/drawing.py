import turtle

def drawEqShape(myturtle = None, num_sides = 0, side_length = 0):
  for i in range(num_sides):
    harold.forward(side_length)
    harold.left(360/num_sides)

harold = turtle.Turtle()
harold.color("green")
harold.shape("turtle")
num_sides = int(input("Pick the number of sides for the shape: "))
side_length = int(input("Pick a length for each side of the shape: "))
drawEqShape(harold, num_sides, side_length)
window = turtle.Screen()
window.exitonclick()