import turtle
import random

def shell(x, y):
  turt.penup()
  turt.goto(x, y)
  turt.pendown()
  turt.color("darkgreen")
  turt.begin_fill()
  turt.right(-20)
  turt.circle(100)
  turt.end_fill()

def leg_code(x = 0, y = 0, angle = 0, degree = 0):
  turt.penup()
  turt.goto(x, y)
  turt.right(angle)
  turt.circle(100, degree)
  turt.pendown()
  turt.color("green")
  turt.begin_fill()
  turt.right(40)
  turt.circle(-20, 300)
  turt.end_fill()
  turt.color("darkgreen")
  
def leg1():
  leg_code(x = x_pos, y = y_pos, degree = 100)

def leg2(x, y): 
  leg_code(x = x_pos, y = y_pos, angle = 120, degree = 230)

def leg3(x, y):
  leg_code(x = x_pos, y = y_pos, angle = 250, degree = 300)

def leg4(x, y): 
  leg_code(x = x_pos, y = y_pos, angle = 320, degree = 30)

def head(x, y):
  turt.penup()
  turt.goto(x, y)
  turt.right(50)
  turt.circle(100, 175)
  turt.pendown()
  turt.color("green")
  turt.begin_fill()
  turt.right(90)
  turt.circle(-30, 213)
  turt.end_fill()
  turt.color("darkgreen")

def eyes():
  turt.penup()
  turt.circle(-30, 190)
  turt.right(70)
  turt.forward(18)
  turt.pendown()
  turt.begin_fill()
  turt.color("black")
  turt.circle(2)
  turt.end_fill()
  turt.penup()
  turt.left(8)
  turt.forward(20)
  turt.pendown()
  turt.begin_fill()
  turt.circle(2)
  turt.end_fill()

def mood():
  mood = random.randrange(1, 5)
  if mood == 1:
    turt.left(45)
    turt.circle(-15, 95)
    return "happy"
  if mood == 2:
    turt.right(45)
    turt.circle(15, 95)
    return "sad"
  if mood == 3:
    turt.forward(22)
    return "bored"
  else:
    turt.left(45)
    turt.circle(-15, 90)
    turt.right(130)
    turt.forward(22)
    return "thrilled"

def main():
  shell(x_pos, y_pos)
  leg1()
  leg2(x_pos, y_pos)
  leg3(x_pos, y_pos)
  leg4(x_pos, y_pos)
  head(x_pos, y_pos)
  eyes()
  turt.penup()
  turt.goto(-20, 120)
  turt.left(180)
  turt.pendown()
  turtmood = mood()
  print("Tortie is feeling", turtmood, "today")
  turt.penup() #so the cursor is not visible
  turt.goto(0, 0)
  turt.color("darkgreen")
  window.bgcolor("lightblue")

x_pos = 0
y_pos = -80
turt = turtle.Turtle()
window = turtle.Screen()
main()

window.exitonclick()
