class Rectangle:
  def __init__(self, x, y, h, w):
    self.x = x
    self.y = y
    self.h = h
    self.w = w

  def __str__(self):
    return f"x: {self.x}, y: {self.y} h: {self.h}, w: {self.w}"