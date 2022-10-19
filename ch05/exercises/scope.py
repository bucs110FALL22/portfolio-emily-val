def multiply(a, b):
  number = 0
  for i in range(b):
    number = number + a
  return number

def exponent(c, d):
  number = 1
  for i in range(d):
    number = number * c
  return number

def square(e):
  return exponent(e, 2)

def main():
  print(multiply(4, 6))
  print(exponent(4, 3))
  print(square(7))

main()
  