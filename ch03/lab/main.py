import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here

michelangelo.forward(random.randrange(1, 101))
leonardo.forward(random.randrange(1, 101))
michelangelo.goto(-100, 20)
leonardo.goto(-100, 20)
for i in range(10):
  michelangelo.forward(random.randrange(1, 10))
  leonardo.forward(random.randrange(1,10))
michelangelo.goto(-100, 20)
leonardo.goto(-100, 20)

# PART B - complete part B here

color = [255, 0, 255]
color2 = [0, 0, 0]
offset = 100
pygame.init()
window = pygame.display.set_mode()
window.fill(color2)


class triangle:
  num_sides = 3
  side_length = 50
  coords = []
for i in range(3):
  theta = (2.0 * math.pi * i)/triangle.num_sides
  x = triangle.side_length * math.cos(theta) + offset
  y = triangle.side_length * math.sin(theta) + offset
  triangle.coords.append((x, y))
pygame.draw.polygon(window, color, triangle.coords)
pygame.display.flip()
pygame.time.wait(1000)
window.fill(color2)
pygame.display.flip()

  
class square:
  num_sides = 4
  side_length = 50
  coords = []
for i in range(3):
  theta = (2.0 * math.pi * i)/square.num_sides
  x = square.side_length * math.cos(theta) + offset
  y = square.side_length * math.sin(theta) + offset
  square.coords.append((x, y))
pygame.draw.polygon(window, color, triangle.coords)
pygame.display.flip()
pygame.time.wait(1000)
window.fill(color2)
pygame.display.flip()

class hexagon:
  num_sides = 6
  side_length = 50
  coords = []
for i in range(3):
  theta = (2.0 * math.pi * i)/hexagon.num_sides
  x = hexagon.side_length * math.cos(theta) + offset
  y = hexagon.side_length * math.sin(theta) + offset
  hexagon.coords.append((x, y))
pygame.draw.polygon(window, color, triangle.coords)
pygame.display.flip()
pygame.time.wait(1000)
window.fill(color2)
pygame.display.flip()

class nonagon: 
  num_sides = 9
  side_length = 50
  coords = []
for i in range(3):
  theta = (2.0 * math.pi * i)/nonagon.num_sides
  x = nonagon.side_length * math.cos(theta) + offset
  y = nonagon.side_length * math.sin(theta) + offset
  nonagon.coords.append((x, y))
pygame.draw.polygon(window, color, triangle.coords)
pygame.display.flip()
pygame.time.wait(1000)
window.fill(color2)
pygame.display.flip()


